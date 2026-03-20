from pathlib import Path
parent_dir = Path(r"E:\Pbaseline")                #定义父文件夹（例如"E:\Pbaseline"）的路径
parent_dir.mkdir(exist_ok=True)                   #确保父文件夹"E:\Pbaseline"存在，，(exist_ok=True): 这是一个参数，意思是“如果这个文件夹已经存在了，也没关系（不要报错），直接跳过”。如果不加这个参数，当你第二次运行程序时，因为文件夹已经存在了，程序就会崩溃报错。
for i in range(1,103):
    folder_path = parent_dir / f"Pbaseline{i}"
    folder_path.mkdir(exist_ok=True)              #.mkdir(): “请在这个路径上创建一个文件夹”；(exist_ok=True): 这是一个参数，意思是“如果这个文件夹已经存在了，也没关系（不要报错），直接跳过”。如果不加这个参数，当你第二次运行程序时，因为文件夹已经存在了，程序就会崩溃报错。
    print(f"已创建或已存在：{folder_path}")
print("批量创建完成！")



