# Python 打印表格

使用`Python`在终端打印出好看的表格
```python
import prettytable
table = PrettyTable(['Title1', 'Title2', 'Title3'])

table.add_row([1, 2, 3])
table.add_row([4, 5, 6])

print(table)
```

效果：

![image](https://cdn.jsdelivr.net/gh/Shanyaliux/PicBed/img/9647f4ca43ae3e82cf9ef49e999c2c0e.webp)