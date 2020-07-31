测试一下 scrapy登录 通过Django的csrf的验证 
首先访问登录界面 找到
<input type="hidden" name="csrfmiddlewaretoken" value="tBW1Dhz7LbdoFHjA2TIhZWikcgaX9nfBLbmVzQnpJJHFZ5NKmIycGxw7Ld5VsKvN">
也就说 这个就是个csrf_token 获取其中的值 然后再使用
spiders 使用from scrapy import FormRequest 登录 添加到data 具体看代码 这样就通过Django的csrf_token验证了