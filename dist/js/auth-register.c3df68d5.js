(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["auth-register"],{"6d75":function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"form auth-boxed"},[s("div",{staticClass:"form-container outer"},[s("div",{staticClass:"form-form"},[s("div",{staticClass:"form-form-wrap"},[s("div",{staticClass:"form-container"},[s("div",{staticClass:"form-content"},[s("h1",{},[e._v("Register")]),s("p",{staticClass:"signup-link register"},[e._v("Already have an account? "),s("router-link",{attrs:{to:"/auth/login-boxed"}},[e._v("Log in")])],1),s("b-form",{staticClass:"text-left",on:{submit:function(t){return t.preventDefault(),e.submit.apply(null,arguments)}}},[s("div",{staticClass:"form"},[s("b-form-invalid-feedback",{staticClass:"text-center",class:{"d-block":e.is_submit_form1&&!e.valid}},[e._v("Username or email already exists!")]),s("b-form-invalid-feedback",{staticClass:"text-center",class:{"d-block":e.is_submit_form1&&(!e.form.password||!e.form.username||!e.form.email)}},[e._v("Please fill all the fields !")]),s("div",{staticClass:"field-wrapper input",attrs:{id:"username-field"}},[s("label",{attrs:{for:"username"}},[e._v("USERNAME")]),s("svg",{staticClass:"feather feather-user",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round"}},[s("path",{attrs:{d:"M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"}}),s("circle",{attrs:{cx:"12",cy:"7",r:"4"}})]),s("b-input",{class:[e.is_submit_form1?e.form.username&&e.form.username.length>=8?"is-valid":"is-invalid":""],attrs:{placeholder:"Username"},model:{value:e.form.username,callback:function(t){e.$set(e.form,"username",t)},expression:"form.username"}}),s("b-form-valid-feedback",[e._v("Looks good!")]),s("b-form-invalid-feedback",{class:{"d-block":e.is_submit_form1&&!e.form.username.length>=8}},[e._v("Please enter a username longer than 8 characters !")])],1),s("div",{staticClass:"field-wrapper input",attrs:{id:"email-field"}},[s("label",{attrs:{for:"email"}},[e._v("Email")]),s("svg",{staticClass:"feather feather-lock",attrs:{xmlns:"http://www.w3.org/2000/svg","aria-hidden":"true",role:"img",width:"1em",height:"1em",preserveAspectRatio:"xMidYMid meet",viewBox:"0 0 20 20"}},[s("path",{attrs:{fill:"currentColor",d:"M14.608 12.172c0 .84.239 1.175.864 1.175c1.393 0 2.28-1.775 2.28-4.727c0-4.512-3.288-6.672-7.393-6.672c-4.223 0-8.064 2.832-8.064 8.184c0 5.112 3.36 7.896 8.52 7.896c1.752 0 2.928-.192 4.727-.792l.386 1.607c-1.776.577-3.674.744-5.137.744c-6.768 0-10.393-3.72-10.393-9.456c0-5.784 4.201-9.72 9.985-9.72c6.024 0 9.215 3.6 9.215 8.016c0 3.744-1.175 6.6-4.871 6.6c-1.681 0-2.784-.672-2.928-2.161c-.432 1.656-1.584 2.161-3.145 2.161c-2.088 0-3.84-1.609-3.84-4.848c0-3.264 1.537-5.28 4.297-5.28c1.464 0 2.376.576 2.782 1.488l.697-1.272h2.016v7.057h.002zm-2.951-3.168c0-1.319-.985-1.872-1.801-1.872c-.888 0-1.871.719-1.871 2.832c0 1.68.744 2.616 1.871 2.616c.792 0 1.801-.504 1.801-1.896v-1.68z"}})]),s("b-input",{class:[e.is_submit_form1?e.form.email&&e.email_validate(e.form.email)?"is-valid":"is-invalid":""],attrs:{placeholder:"Email@email.com",type:"email"},model:{value:e.form.email,callback:function(t){e.$set(e.form,"email",t)},expression:"form.email"}}),s("b-form-valid-feedback",[e._v("Looks good!")]),s("b-form-invalid-feedback",{class:{"d-block":e.is_submit_form1&&!e.email_validate(e.form.email)}},[e._v("Please fill a correct email !")])],1),s("div",{staticClass:"field-wrapper input mb-2",attrs:{id:"password-field"}},[s("div",{staticClass:"d-flex justify-content-between"},[s("label",{attrs:{for:"password"}},[e._v("PASSWORD")]),s("router-link",{staticClass:"forgot-pass-link",attrs:{to:"/auth/pass-recovery-boxed"}},[e._v("Forgot Password?")])],1),s("svg",{staticClass:"feather feather-lock",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round"}},[s("rect",{attrs:{x:"3",y:"11",width:"18",height:"11",rx:"2",ry:"2"}}),s("path",{attrs:{d:"M7 11V7a5 5 0 0 1 10 0v4"}})]),s("b-input",{class:[e.is_submit_form1?e.form.password&&e.form.password.length>=8?"is-valid":"is-invalid":""],attrs:{type:e.pwd_type,placeholder:"Password"},model:{value:e.form.password,callback:function(t){e.$set(e.form,"password",t)},expression:"form.password"}}),s("svg",{staticClass:"feather feather-eye",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round",id:"toggle-password"},on:{click:e.set_pwd_type}},[s("path",{attrs:{d:"M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"}}),s("circle",{attrs:{cx:"12",cy:"12",r:"3"}})]),s("b-form-valid-feedback",[e._v("Looks good!")]),s("b-form-invalid-feedback",{class:{"d-block":e.is_submit_form1&&!e.form.password.length>=8}},[e._v("Please enter a password longer than 8 characters !")])],1),s("b-form-checkbox",{staticClass:"text-white mb-3",attrs:{id:"checkbox-1",name:"checkbox-1",value:"1"},model:{value:e.check,callback:function(t){e.check=t},expression:"check"}},[s("p",[e._v("I am an entreprise")])]),s("div",{staticClass:"d-sm-flex justify-content-between"},[s("div",{staticClass:"field-wrapper"},[s("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Get Started!")])],1)]),s("div",{staticClass:"division"},[s("span",[e._v("OR")])]),s("div",{staticClass:"social"},[s("a",{staticClass:"google-signup",attrs:{href:"#"},on:{click:function(t){return t.preventDefault(),e.loginWithGoogle.apply(null,arguments)}}},[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",width:"18",height:"18",viewBox:"0 0 18 18","aria-hidden":"true"}},[s("title",[e._v("Google")]),s("g",{attrs:{fill:"none","fill-rule":"evenodd"}},[s("path",{attrs:{fill:"#4285F4",d:"M17.64 9.2045c0-.6381-.0573-1.2518-.1636-1.8409H9v3.4814h4.8436c-.2086 1.125-.8427 2.0782-1.7959 2.7164v2.2581h2.9087c1.7018-1.5668 2.6836-3.874 2.6836-6.615z"}}),s("path",{attrs:{fill:"#34A853",d:"M9 18c2.43 0 4.4673-.806 5.9564-2.1805l-2.9087-2.2581c-.8059.54-1.8368.859-3.0477.859-2.344 0-4.3282-1.5831-5.036-3.7104H.9574v2.3318C2.4382 15.9832 5.4818 18 9 18z"}}),s("path",{attrs:{fill:"#FBBC05",d:"M3.964 10.71c-.18-.54-.2822-1.1168-.2822-1.71s.1023-1.17.2823-1.71V4.9582H.9573A8.9965 8.9965 0 0 0 0 9c0 1.4523.3477 2.8268.9573 4.0418L3.964 10.71z"}}),s("path",{attrs:{fill:"#EA4335",d:"M9 3.5795c1.3214 0 2.5077.4541 3.4405 1.346l2.5813-2.5814C13.4632.8918 11.426 0 9 0 5.4818 0 2.4382 2.0168.9573 4.9582L3.964 7.29C4.6718 5.1627 6.6559 3.5795 9 3.5795z"}})])]),e._v(" Google ")])])],1)])],1)])])])])])},r=[],i=s("1da1"),o=s("5530"),l=(s("96cf"),s("ac1f"),s("00b4"),s("fb6a"),s("2f62")),n=(s("ce14"),{metaInfo:{title:"Register Boxed"},data:function(){return{check:null,pwd_type:"password",form:{username:"",email:"",password:""},valid:!0,is_submit_form1:!1}},methods:Object(o["a"])(Object(o["a"])({},Object(l["b"])(["CreateRole","isEntreprise","Register"])),{},{set_pwd_type:function(){"password"==this.pwd_type?this.pwd_type="text":this.pwd_type="password"},email_validate:function(e){var t=/^[\w.%+-]+@[\w.-]+\.[\w]{2,6}$/;return t.test(e)},submit:function(){var e=this;return Object(i["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(e.is_submit_form1=!0,!(e.form.username&&e.form.username.length>=8&&e.form.password.length>=8&&e.form.password&&e.form.email)){t.next=22;break}return t.prev=2,console.log("wa"),t.next=6,e.Register(e.form);case 6:if(null!=e.check){t.next=12;break}return t.next=9,e.isEntreprise(!1);case 9:e.$router.push("/auth/userinfo"),t.next=16;break;case 12:if(1!=e.check){t.next=16;break}return t.next=15,e.isEntreprise(!0);case 15:e.$router.push("/auth/userentrepriseinfo");case 16:t.next=22;break;case 18:t.prev=18,t.t0=t["catch"](2),console.log(t.t0),e.valid=!1;case 22:case"end":return t.stop()}}),t,null,[[2,18]])})))()},loginWithGoogle:function(){var e=this;this.$gAuth.signIn().then((function(t){var s={loginType:"google",google:{auth:t.getAuthResponse(),user:{name:t.getBasicProfile().getName(),email:t.getBasicProfile().getEmail(),profileImage:t.getBasicProfile().getImageUrl(),username:t.getBasicProfile().getEmail().toLowerCase().slice(0,t.getBasicProfile().getEmail().indexOf("@"))}}};e.Register({username:s.google.user.username,email:s.google.user.email,password:"ggddbxcxw54cwxc5xw4c8s848qc61sc1q9c4dsv1fdbg894nf6bfjf"}),e.$store.commit("setLoginUser",s),e.$router.push("/")}))}})}),c=n,d=s("2877"),m=Object(d["a"])(c,a,r,!1,null,null,null);t["default"]=m.exports},ce14:function(e,t,s){}}]);
//# sourceMappingURL=auth-register.c3df68d5.js.map