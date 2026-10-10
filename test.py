# 用事件循环队列实现生产者-消费者异步流程
import asyncio
import time

async def consumer(q):
    print('consumer starts.')
    while True:
        item = await q.get()  # 从队列获取数据（如果没有则等待）
        
        if item is None:      # None 是结束信号
            q.task_done()
            break
        else:
            await asyncio.sleep(0.1)  # 模拟消费耗时
            print('consume %d' % item)
            q.task_done()      # 通知队列一个任务已完成
    
    print('consumer ends.')

async def producer(q):
    print('producer starts.')
    
    for i in range(5):
        await asyncio.sleep(0.1)  # 模拟生产耗时
        print('produce %d' % i)
        await q.put(i)          # 放入队列
    
    await q.put(None)           # 发送结束信号
    await q.join()              # 等待所有消费完成
    print('producer ends.')

# 主程序
q = asyncio.Queue(maxsize=10)
t0 = time.time()
loop = asyncio.get_event_loop() # 获取当前事件循环
tasks = [producer(q), consumer(q)]
loop.run_until_complete(asyncio.wait(tasks))
# asyncio.wait(tasks) 创建一个新的协程，等待多个任务完成
# loop.run_until_complete() 启动事件循环，运行指定的协程直到它完成
loop.close() # 关闭事件循环，释放资源
print(time.time() - t0, "s")
