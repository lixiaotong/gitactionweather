# 自动获取天气信息，发送到邮箱

## 基本概念
### GitHub Actions 有一些自己的术语。
1. workflow （工作流程）：持续集成一次运行的过程，就是一个 workflow。
2. job （任务）：一个 workflow 由一个或多个 jobs 构成，含义是一次持续集成的运行，可以完成多个任务。
3. step（步骤）：每个 job 由多个 step 构成，一步步完成。
4. action （动作）：每个 step 可以依次执行一个或多个命令（action）

    
    name: 'GitHub Actions CSDN Email Bot'  
      on:       
      push:         
        branches:       
          - master      
      schedule:        
        - cron: '0 14 * * *'   
     

name 是该配置文件的名字. 
on 是触发条件，我们指定两种情况下触发.     
  第一种是向 master 分支 push 代码时触发，   
  第二种是定时任务，每天在国际标准时间 14 点（北京时间 22 点）运行.   

需要注意的是，必须使用 POSIX cron 语法 安排工作流程在特定的 UTC 时间（国际标准时间，等于北京时间减去 8 个小时）运行，并且最短间隔为每 5 分钟一次. 

计划任务语法有五个字段，中间用空格分隔，每个字段代表一个时间单位. 

┌───────────── minute (0 - 59)  
│ ┌───────────── hour (0 - 23)  
│ │ ┌───────────── day of the month (1 - 31)  
│ │ │ ┌───────────── month (1 - 12 or JAN-DEC)  
│ │ │ │ ┌───────────── day of the week (0 - 6 or SUN-SAT)  
│ │ │ │ │    
│ │ │ │ │    



可在这五个字段中使用以下运算符：

运算符 描述 示例

    任意值 * * * * * 在每天的每分钟运行
    , 值列表分隔符 2,10 4,5 * * * 在每天第 4 和第 5 小时的第 2 和第 10 分钟运行

    值的范围 0 4-6 * * * 在第 4、5、6 小时的第 0 分钟运行
    / 步骤值 20/15 * * * * 从第 20 分钟到第 59 分钟每隔 15 分钟运行（第 20、35 和 50 分钟）
    注：GitHub 操作 不支持非标准语法 @yearly、@monthly、@weekly、@daily、@hourly 和 @reboot
