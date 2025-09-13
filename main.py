print("未来10年地球和月球体重预测")
earth_weight=float(input("请输入你当前体重(公斤)："))
moon_ratio=0.165
year_gain=0.5

print("{:<5}{:<10}{:<10}".format("年","地球体重","月球体重"))
for year in range(1,11):
    earth_current=earth_weight+year*year_gain
    moon_current=earth_current*moon_ratio
    print("{:<5}{:<10.2f}{:<10.2f}".format(year,earth_current,moon_current))
