import asyncio
n=int(input("Enter the number of timers you want to set: "))
l=[]
for i in range(n):
    name = input(f"Enter name for timer {i+1}: ")
    t = int(input(f"Enter time for timer {i+1} (in seconds): "))
    l.append((name, t))

async def main():
    tasks = [asyncio.create_task(countdown(name, t)) for name, t in l]
    await asyncio.gather(*tasks)

async def countdown(name, t):
    while t>0:
        print(f"{name} timer : {t}")
        await asyncio.sleep(1)
        t-=1
    print(f"{name} timer : Time's up!")

if __name__ == "__main__":
    asyncio.run(main())

    