# chattig-group

# If you want run same device or local network--

1. First of all open terminal and run server.py file

2. then run new terminal chat_page.py

3. again open new terminal and run again chat_page.py

4. then put different name both output 





![IMG_20220501_223358](https://user-images.githubusercontent.com/92147303/166157222-f42d01c5-71f4-40e2-864c-f66882171c33.jpg)






![IMG_20220501_223501](https://user-images.githubusercontent.com/92147303/166157237-c6aa67e3-03a5-4ad1-9309-14b25ab7c143.jpg)




![IMG_20220501_223543](https://user-images.githubusercontent.com/92147303/166157238-e97bdc0e-6568-4510-bb63-ab95728bf6fb.jpg)

# If you want to run different system then you will some change.

#changes---

#1. do change in server.py file in line 5 

    server.bind(("localhost",5501)) --> server.bind(("put public ip",port))

#2.  do change in chat_page.py file in line 40

     client.connect(("localhost",5501)) --> client.connect(("public ip",port))


