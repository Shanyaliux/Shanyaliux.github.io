# 常用的shell脚本

## for 循环

```bash
for i in $(seq 1 5)  
do   
# code
done
```

## 遍历文件夹名

```bash
dir=$(ls -l $1 |awk '/^d/ {print $NF}')
echo $1
for i in $dir
do
 echo $i
done
```

