## 功能介绍
1、	Ajax实现用户注册、登录，涉及功能：运用pillow模块自定义验证码并保存在session中通过form全局钩子进行验证、formdata上传图片、利用Js实现图片动态显示；
2、	评论渲染的三种方式：
    a)	常规评论，在子评论上方追加父评论内容；
    b)	评论树结构，页面加载后发送再次ajax请求评论信息，在js中动态组装评论信息，后加载到html中；
    c)	评论树结构，自定义标签渲染，直接渲染到页面中；

3、前端通过jquery拼接节点动态添加新提交的评论；