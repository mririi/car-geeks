(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-034544b0"],{"0bec":function(e,t,s){"use strict";s.r(t);var r=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"layout-px-spacing"},[s("portal",{attrs:{to:"breadcrumb"}},[s("ul",{staticClass:"navbar-nav flex-row"},[s("li",[s("div",{staticClass:"page-header"},[s("nav",{staticClass:"breadcrumb-one",attrs:{"aria-label":"breadcrumb"}},[s("ol",{staticClass:"breadcrumb"},[s("li",{staticClass:"breadcrumb-item"},[s("a",{attrs:{href:"javascript:;"}},[e._v("Dashboard")])]),s("li",{staticClass:"breadcrumb-item active",attrs:{"aria-current":"page"}},[s("span",[e._v("Questions Request")])])])])])])])]),s("div",{staticClass:"row layout-top-spacing"},[s("div",{staticClass:"col-xl-12 col-lg-12 col-sm-12 layout-spacing"},[s("div",{staticClass:"panel p-0"},[s("div",{staticClass:"custom-table table3"},[s("div",{staticClass:"table-header"},[s("div",{staticClass:"d-flex align-items-center"},[s("span",[e._v("Results :")]),s("span",{staticClass:"ml-2"},[s("b-select",{staticClass:"h-auto",model:{value:e.table_option2.page_size,callback:function(t){e.$set(e.table_option2,"page_size",t)},expression:"table_option2.page_size"}},[s("b-select-option",{attrs:{value:"5"}},[e._v("5")]),s("b-select-option",{attrs:{value:"10"}},[e._v("10")]),s("b-select-option",{attrs:{value:"20"}},[e._v("20")]),s("b-select-option",{attrs:{value:"50"}},[e._v("50")])],1)],1),s("span",{directives:[{name:"b-toggle",rawName:"v-b-toggle.collapse-1",modifiers:{"collapse-1":!0}}],staticClass:"ml-2 mt-2 justify-content-end"},[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg","aria-hidden":"true",role:"img",width:"22",height:"20",preserveAspectRatio:"xMidYMid meet",viewBox:"0 0 36 36"}},[s("path",{staticClass:"clr-i-solid clr-i-solid-path-1",attrs:{fill:"currentColor",d:"M22 33V19.5L33.47 8A1.81 1.81 0 0 0 34 6.7V5a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1.67a1.79 1.79 0 0 0 .53 1.27L14 19.58v10.2Z"}}),s("path",{staticClass:"clr-i-solid clr-i-solid-path-1",attrs:{fill:"currentColor",d:"M33.48 4h-31a.52.52 0 0 0-.48.52v1.72a1.33 1.33 0 0 0 .39.95l12 12v10l7.25 3.61V19.17l12-12a1.35 1.35 0 0 0 .36-.91V4.52a.52.52 0 0 0-.52-.52Z"}}),s("path",{attrs:{fill:"none",d:"M0 0h36v36H0z"}})]),s("span",{staticClass:"h6"},[e._v("Filter")])])]),s("b-collapse",{attrs:{id:"collapse-1"}},[s("b-card",{staticClass:"bg-transparent border-0 border-white ml-3 default mt-2 mb-4"},[s("b-form-group",{attrs:{label:"Categories : "},scopedSlots:e._u([{key:"default",fn:function(t){var r=t.ariaDescribedby;return[s("b-form-checkbox-group",{attrs:{id:"checkbox-group-2","aria-describedby":r,name:"flavour-a1"},model:{value:e.category,callback:function(t){e.category=t},expression:"category"}},e._l(e.Questioncategories,(function(t){return s("div",{key:t.id},[s("b-form-checkbox",{attrs:{value:t.id}},[e._v(" "+e._s(t.typeC)+" ")])],1)})),0)]}}])})],1)],1),s("div",{staticClass:"header-search"},[s("b-input",{attrs:{size:"sm",placeholder:"Search..."},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}}),s("div",{staticClass:"search-image"},[s("svg",{staticClass:"feather feather-search",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round"}},[s("circle",{attrs:{cx:"11",cy:"11",r:"8"}}),s("line",{attrs:{x1:"21",y1:"21",x2:"16.65",y2:"16.65"}})])])],1)],1),s("b-table",{ref:"basic_table2",attrs:{responsive:"",hover:"",bordered:"",items:e.filterByCategory,fields:e.columns2,"per-page":e.table_option2.page_size,"current-page":e.table_option2.current_page,filter:e.table_option2.search_text,"sort-by":"id","show-empty":!0},on:{filtered:e.on_filtered,"sort-changed":e.clear_selection},scopedSlots:e._u([{key:"cell(accepted)",fn:function(){return[s("span",[s("b-badge",{attrs:{variant:"danger"}},[e._v("Pending")])],1)]},proxy:!0},{key:"cell(dateQ)",fn:function(t){return[e._v(" "+e._s(e._f("formatDate")(t.item.dateQ))+" ")]}},{key:"cell(userprofileQ)",fn:function(t){return[null!=t.item.userprofileQ?s("span",e._l(e.Userprofiles,(function(r){return s("span",{key:r.id},[r.id==t.item.userprofileQ?s("span",[s("router-link",{attrs:{to:"/profile/"+t.item.userprofileQ}},[e._v(" "+e._s(r.firstname)+" "+e._s(r.lastname)+" ")])],1):e._e()])})),0):e._e(),null!=t.item.userentrepriseQ?s("span",e._l(e.Userentreprises,(function(r){return s("span",{key:r.id},[r.id==t.item.userentrepriseQ?s("span",[s("router-link",{attrs:{to:"/entreprisedetails/"+t.item.userentrepriseQ}},[e._v(" "+e._s(r.nameE)+" ")])],1):e._e()])})),0):e._e()]}},{key:"cell(categoryQ)",fn:function(t){return e._l(e.Questioncategories,(function(r){return s("span",{key:r.id},[r.id==t.item.categoryQ?s("span",[e._v(" "+e._s(r.typeC)+" ")]):e._e()])}))}},{key:"cell(actions)",fn:function(t){return[s("span",{on:{click:function(s){return e.Accept(t.item)}}},[s("svg",{staticClass:"feather feather-check-circle text-primary ac",attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor","stroke-width":"2","stroke-linecap":"round","stroke-linejoin":"round"}},[s("path",{attrs:{d:"M22 11.08V12a10 10 0 1 1-5.93-9.14"}}),s("polyline",{attrs:{points:"22 4 12 14.01 9 11.01"}})])])]}},{key:"cell(imageQ)",fn:function(e){return[null!=e.item.imageQ?s("span",[s("b-avatar",{attrs:{src:"https://cargeeks.herokuapp.com"+e.item.imageQ,size:"4rem",rounded:"lg",alt:"",srcset:""}})],1):s("span",[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg","aria-hidden":"true",role:"img",width:"4em",height:"4em",preserveAspectRatio:"xMidYMid meet",viewBox:"0 0 64 64"}},[s("path",{attrs:{fill:"currentColor",d:"M32 2C15.432 2 2 15.432 2 32.001C2 48.567 15.432 62 32 62s30-13.433 30-29.999C62 15.432 48.568 2 32 2zm22 30.001c0 4.629-1.433 8.922-3.876 12.465l-30.591-30.59A21.889 21.889 0 0 1 32 10c12.15 0 22 9.851 22 22.001zm-44 0a21.9 21.9 0 0 1 3.876-12.468l30.591 30.591A21.887 21.887 0 0 1 32 54.001c-12.15 0-22-9.852-22-22z"}})])])]}}])}),s("div",{staticClass:"table-footer"},[s("div",{staticClass:"dataTables_info"},[e._v("Showing "+e._s(e.meta2.total_items?e.meta2.start_index+1:0)+" to "+e._s(e.meta2.end_index+1)+" of "+e._s(e.meta2.total_items))]),s("div",{staticClass:"paginating-container pagination-solid flex-column align-items-right"},[s("b-pagination",{staticClass:"rounded",attrs:{"total-rows":e.table_option2.total_rows,"per-page":e.table_option2.page_size,"prev-text":"Prev","next-text":"Next","first-text":"First","last-text":"Last","first-class":"first","prev-class":"prev","next-class":"next","last-class":"last"},scopedSlots:e._u([{key:"first-text",fn:function(){return[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"}},[s("path",{attrs:{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M11 19l-7-7 7-7m8 14l-7-7 7-7"}})])]},proxy:!0},{key:"prev-text",fn:function(){return[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"}},[s("path",{attrs:{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M15 19l-7-7 7-7"}})])]},proxy:!0},{key:"next-text",fn:function(){return[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"}},[s("path",{attrs:{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M9 5l7 7-7 7"}})])]},proxy:!0},{key:"last-text",fn:function(){return[s("svg",{attrs:{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"}},[s("path",{attrs:{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M13 5l7 7-7 7M5 5l7 7-7 7"}})])]},proxy:!0}]),model:{value:e.table_option2.current_page,callback:function(t){e.$set(e.table_option2,"current_page",t)},expression:"table_option2.current_page"}})],1)])],1)])])])],1)},i=[],a=s("1da1"),n=s("5530"),o=(s("96cf"),s("4de4"),s("d3b7"),s("caad"),s("2532"),s("ac1f"),s("841c"),s("d81d"),s("a630"),s("3ca3"),s("ddb0"),s("2f62")),l=s("bc3a"),c=s.n(l),u={metaInfo:{title:"Bootstrap Custom Table"},data:function(){return{items2:[],columns2:[],table_option2:{total_rows:0,current_page:1,page_size:5,search_text:""},meta2:{},is_select_all2:!1,selected_rows2:[],search:"",category:"",uentreprise:[],uprofile:[]}},watch:{table_option:{handler:function(){this.get_meta(),this.clear_selection()},deep:!0},table_option1:{handler:function(){this.get_meta1(),this.clear_selection1()},deep:!0},table_option2:{handler:function(){this.get_meta2(),this.clear_selection2()},deep:!0}},created:function(){this.GetQuestions(),this.GetUserprofiles(),this.GetQuestioncategories(),this.GetUsers(),this.GetUserentreprises()},mounted:function(){this.bind_data()},computed:Object(n["a"])(Object(n["a"])({},Object(o["c"])({Questions:"StateQuestions",Userprofiles:"StateUserprofiles",Questioncategories:"StateQuestioncategories",Userentreprises:"StateUserentreprises",User:"StateUser",Users:"StateUsers"})),{},{filteredList:function(){var e=this;return this.Questions.filter((function(t){return t.titleQ.toLowerCase().includes(e.search.toLowerCase())&&0==t.accepted}))},filterByCategory:function(){var e=this;return""!=this.category?this.filteredList.filter((function(t){return e.category.includes(t.categoryQ)})):this.filteredList}}),methods:Object(n["a"])(Object(n["a"])({},Object(o["b"])(["GetQuestions","CreateNotification","GetUsers","GetUserprofiles","GetQuestioncategories","GetUserentreprises"])),{},{Accept:function(e){var t=this;return Object(a["a"])(regeneratorRuntime.mark((function s(){return regeneratorRuntime.wrap((function(s){while(1)switch(s.prev=s.next){case 0:t.$swal({icon:"warning",title:"Are you sure?",showCancelButton:!0,confirmButtonText:"Accept",padding:"2em"}).then((function(s){if(s.value){if(c.a.put("/question/question-update/"+e.id+"/",{accepted:!0}),null!=e.userprofileQ){for(var r in t.Userprofiles)if(t.Userprofiles[r].id==e.userprofileQ)for(var i in t.Questions)t.Questions[i].id==e.id&&0==t.Questions[i].modified&&(c.a.put("/userprofile/userprofile-update/"+e.userprofileQ+"/",{nbquestions:t.Userprofiles[r].nbquestions+=1}),t.CreateNotification({message:"Your Question has been accepted !",questionNo:e.id,userprofileNo:e.userprofileQ,userentrepriseNo:e.userentrepriseQ,admin:!0}))}else if(null!=e.userentrepriseQ)for(var a in t.Userentreprises)if(t.Userentreprises[a].id==e.userentrepriseQ)for(var n in t.Questions)t.Questions[n].id==e.id&&0==t.Questions[n].modified&&(c.a.put("/userentreprise/userentreprise-update/"+e.userentrepriseQ+"/",{nbquestions:t.Userentreprises[a].nbquestions+=1}),t.CreateNotification({message:"Your Question has been accepted ",questionNo:t.Questions[n].id,entrepriseNo:e.userentrepriseQ,admin:!0}));t.$swal("Accepted!","The question has been accepted.","success"),t.$router.go()}}));case 1:case"end":return s.stop()}}),s)})))()},bind_data:function(){this.columns2=[{key:"imageQ",label:"Image",class:"text-center  "},{key:"titleQ",label:"Title"},{key:"contentQ",label:"Content"},{key:"dateQ",label:"Date"},{key:"categoryQ",label:"Category"},{key:"nbrep",label:"Replies"},{key:"userprofileQ",label:"User"},{key:"accepted",label:"Status",class:"text-center  "},{key:"actions",label:"Actions",class:"text-center  "}],this.table_option2.total_rows=this.filterByCategory.length,this.get_meta2()},on_filtered:function(e){this.refresh_table(e.length)},refresh_table:function(e){this.table_option.total_rows=e,this.table_option.currentPage=1},get_meta:function(){this.meta=this.get_common_meta(this.table_option)},get_common_meta:function(e){var t,s,r=e.page_size<1?1:Math.ceil(e.total_rows/e.page_size);r=Math.max(r||0,1);var i=5,a="undefined"!==typeof i&&i<r;a?(t=Math.max(e.current_page-Math.floor(i/2),1),s=t+i-1,s>r&&(s=r,t=s-i+1)):(t=1,s=r);var n=(e.current_page-1)*e.page_size,o=Math.min(n+e.page_size-1,e.total_rows-1),l=Array.from(Array(s+1-t).keys()).map((function(e){return t+e}));return{total_items:e.total_rows,current_page:e.current_page,page_size:e.page_size,total_pages:r,start_page:t,end_page:s,start_index:n,end_index:o,pages:l}},select_all:function(){this.selected_rows=this.$refs.basic_table.paginatedItems.map((function(e){return e.id})),this.is_select_all||this.clear_selection(),this.check_select_all()},check_select_all:function(){var e=this.$refs.basic_table.paginatedItems.map((function(e){return e.id}));this.is_select_all=!1,e.length==this.selected_rows.length&&(this.is_select_all=!0)},clear_selection:function(){this.is_select_all=!1,this.selected_rows=[]},on_filtered1:function(e){this.refresh_table1(e.length)},refresh_table1:function(e){this.table_option1.total_rows=e,this.table_option1.currentPage=1},get_meta1:function(){this.meta1=this.get_common_meta(this.table_option1)},select_all1:function(){this.selected_rows1=this.$refs.basic_table1.paginatedItems.map((function(e){return e.id})),this.is_select_all1||this.clear_selection1(),this.check_select_all1()},check_select_all1:function(){var e=this.$refs.basic_table1.paginatedItems.map((function(e){return e.id}));this.is_select_all1=!1,e.length==this.selected_rows1.length&&(this.is_select_all1=!0)},clear_selection1:function(){this.is_select_all1=!1,this.selected_rows1=[]},on_filtered2:function(e){this.refresh_table2(e.length)},refresh_table2:function(e){this.table_option2.total_rows=e,this.table_option2.currentPage=1},get_meta2:function(){this.meta2=this.get_common_meta(this.table_option2)},select_all2:function(){this.selected_rows2=this.$refs.basic_table2.paginatedItems.map((function(e){return e.id})),this.is_select_all2||this.clear_selection2(),this.check_select_all2()},check_select_all2:function(){var e=this.$refs.basic_table2.paginatedItems.map((function(e){return e.id}));this.is_select_all2=!1,e.length==this.selected_rows2.length&&(this.is_select_all2=!0)},clear_selection2:function(){this.is_select_all2=!1,this.selected_rows2=[]}})},p=u,d=(s("99ce"),s("2877")),h=Object(d["a"])(p,r,i,!1,null,null,null);t["default"]=h.exports},2532:function(e,t,s){"use strict";var r=s("23e7"),i=s("e330"),a=s("5a34"),n=s("1d80"),o=s("577e"),l=s("ab13"),c=i("".indexOf);r({target:"String",proto:!0,forced:!l("includes")},{includes:function(e){return!!~c(o(n(this)),o(a(e)),arguments.length>1?arguments[1]:void 0)}})},"44e7":function(e,t,s){var r=s("861d"),i=s("c6b6"),a=s("b622"),n=a("match");e.exports=function(e){var t;return r(e)&&(void 0!==(t=e[n])?!!t:"RegExp"==i(e))}},"4df4":function(e,t,s){"use strict";var r=s("da84"),i=s("0366"),a=s("c65b"),n=s("7b0b"),o=s("9bdd"),l=s("e95a"),c=s("68ee"),u=s("07fa"),p=s("8418"),d=s("9a1f"),h=s("35a1"),f=r.Array;e.exports=function(e){var t=n(e),s=c(this),r=arguments.length,_=r>1?arguments[1]:void 0,g=void 0!==_;g&&(_=i(_,r>2?arguments[2]:void 0));var b,m,v,w,x,y,k=h(t),C=0;if(!k||this==f&&l(k))for(b=u(t),m=s?new this(b):f(b);b>C;C++)y=g?_(t[C],C):t[C],p(m,C,y);else for(w=d(t,k),x=w.next,m=s?new this:[];!(v=a(x,w)).done;C++)y=g?o(w,_,[v.value,C],!0):v.value,p(m,C,y);return m.length=C,m}},"5a34":function(e,t,s){var r=s("da84"),i=s("44e7"),a=r.TypeError;e.exports=function(e){if(i(e))throw a("The method doesn't accept regular expressions");return e}},"99ce":function(e,t,s){"use strict";s("9baa")},"9baa":function(e,t,s){},"9bdd":function(e,t,s){var r=s("825a"),i=s("2a62");e.exports=function(e,t,s,a){try{return a?t(r(s)[0],s[1]):t(s)}catch(n){i(e,"throw",n)}}},a630:function(e,t,s){var r=s("23e7"),i=s("4df4"),a=s("1c7e"),n=!a((function(e){Array.from(e)}));r({target:"Array",stat:!0,forced:n},{from:i})},ab13:function(e,t,s){var r=s("b622"),i=r("match");e.exports=function(e){var t=/./;try{"/./"[e](t)}catch(s){try{return t[i]=!1,"/./"[e](t)}catch(r){}}return!1}},caad:function(e,t,s){"use strict";var r=s("23e7"),i=s("4d64").includes,a=s("44d2");r({target:"Array",proto:!0},{includes:function(e){return i(this,e,arguments.length>1?arguments[1]:void 0)}}),a("includes")},d81d:function(e,t,s){"use strict";var r=s("23e7"),i=s("b727").map,a=s("1dde"),n=a("map");r({target:"Array",proto:!0,forced:!n},{map:function(e){return i(this,e,arguments.length>1?arguments[1]:void 0)}})}}]);
//# sourceMappingURL=chunk-034544b0.51b80069.js.map