# Channel Talk 구현

1. 채널톡 페이지 가입 후, 제공되는 자바스크립트 코드를 붙이면 된다.

```javascript
(function(){var w=window;if(w.ChannelIO){return w.console.error("ChannelIO script included twice.");}var ch=function(){ch.c(arguments);};ch.q=[];ch.c=function(args){ch.q.push(args);};w.ChannelIO=ch;function l(){if(w.ChannelIOInitialized){return;}w.ChannelIOInitialized=true;var s=document.createElement("script");s.type="text/javascript";s.async=true;s.src="https://cdn.channel.io/plugin/ch-plugin-web.js";var x=document.getElementsByTagName("script")[0];if(x.parentNode){x.parentNode.insertBefore(s,x);}}if(document.readyState==="complete"){l();}else{w.addEventListener("DOMContentLoaded",l);w.addEventListener("load",l);}})();
  
    ChannelIO('boot', {
      "pluginKey": "e9460f81-7a6f-442d-8f93-23a70f8e892b"
    });
```

2. 사이트 가입 후 생성되는 개인 채널톡 채널에서 간단한 커스터마이징이 가능하며, 모바일 버전 등은 추가적으로 결제가 필요하다