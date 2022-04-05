<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Apps</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Chat</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="chat-section layout-top-spacing">
      <div class="row">
        <div class="col-xl-12 col-lg-12 col-md-12">
          <div class="chat-system">
            <div class="hamburger" @click="is_show_user_menu = !is_show_user_menu">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-menu mail-menu d-lg-none"
              >
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
              </svg>
            </div>
            <div class="user-list-box" :class="{ 'user-list-box-show': is_show_user_menu }">
              <div class="search">
                  <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      class="feather feather-search"
                  >
                      <circle cx="11" cy="11" r="8"></circle>
                      <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                  <b-input v-model="search" placeholder="Search User" @keyup="search" />
              </div>
              <perfect-scrollbar class="people" :options="{ wheelSpeed: 0.5, swipeEasing: !0, minScrollbarLength: 40, maxScrollbarLength: 300, suppressScrollX: true }">
                <div v-for="person in filteredList" class="person" :key="person.id" :class="{ active: selected_user && selected_user.id == person.id }" @click="select_user(person)">
                  <div class="user-info">
                    <div class="f-head">
                      <img :src="person.imageU" alt="avatar" />
                    </div>
                    <div class="f-body">
                      <div class="meta-info">
                        <span class="user-name" :class="{ 'text-primary': selected_user && selected_user.id == person.id }">{{ person.firstname }}</span>
                      </div>
                      <span class="preview"> <div>{{preview(person)}}</div></span>
                    </div>
                  </div>
                </div>
              </perfect-scrollbar>
            </div>
            <div class="chat-box" :class="{ active: selected_user }">
              <div class="chat-not-selected" :class="{ 'd-none': selected_user }">
                <p>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="feather feather-message-square"
                  >
                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                  </svg>
                  Click User To Chat
                </p>
              </div>

              <div v-if="selected_user" class="chat-box-inner h-100">
                <div class="chat-meta-user chat-active">
                  <div class="current-chat-user-name">
                    <span>
                      <img :src="selected_user.imageU" alt="dynamic-image" />
                      <span class="name">{{ selected_user.firstname }} {{ selected_user.lastname }}</span>
                    </span>
                  </div>
                </div>
                <perfect-scrollbar class="chat-conversation-box" 
                :options="{ wheelSpeed: 1.5, swipeEasing: !0, minScrollbarLength: 40, maxScrollbarLength: 300, suppressScrollX: true }">
                  <div id="chat-conversation-box-scroll" class="chat-conversation-box-scroll">
                    <div class="chat active-chat">
                      <template>
                        <div v-for="(chat,index) in messages" :key="'msg' + index">
                          <div v-if="(chat.reciever == selected_user.userU && chat.sender==CurrentUser.id) || (chat.sender == selected_user.userU && chat.reciever== CurrentUser.id)" class="bubble" :class="[selected_user.userU == chat.reciever ? 'me' : 'you']">
                            {{ chat.message }}
                          </div>
                        </div>
                      </template>
                    </div>
                  </div>
                </perfect-scrollbar>
                <div class="chat-footer chat-active">
                  <div class="chat-input">
                    <div class="chat-form">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="feather feather-message-square"
                      >
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                      </svg>
                      <b-input v-model="text_message" class="mail-write-box" placeholder="Message" @keyup.enter.exact="send_message" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import '@/assets/sass/apps/chat.scss';
import { mapGetters, mapActions } from 'vuex';
import Pusher from 'pusher-js';
export default {
  metaInfo: { title: 'Chat Application' },
  components: {},
  data() {
    return {
      is_show_user_menu: false,
      selected_user: null,
      text_message: '',
      CurrentUser: [],
      senders: [],
      messages: [],
      search: '',
      Contactlist:[]
    };
  },
  computed: {
    ...mapGetters({
      User: 'StateUser',
      Users: 'StateUsers',
      Chats: 'StateChats',
      Userprofiles: 'StateUserprofiles',
    }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
    
    filteredList() {
      return this.Contactlist.filter((user) => {
        return user.firstname.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    
  },
  mounted() {
    var pusher = new Pusher('027d486814c2e9262191', {
      cluster: 'eu',
    });
    let messages = this.messages;
    var channel = pusher.subscribe('chat');
    channel.bind('message', function (data) {
      let l = messages[messages.length - 1].id + 1;
      messages.push({ id: l, message: data.chats.message, sender: data.chats.sender, reciever: data.chats.reciever, dateCh: null, preview: '' });
      this.messages = messages;
      setTimeout(() => {
        document.querySelector('.chat-conversation-box').scrollTo({ left: 0, top: document.querySelector('.chat-conversation-box').scrollHeight, behavior: 'smooth' });
      });
    });
  },
  methods: {
    ...mapActions(['GetUsers', 'CreateChat', 'GetUserprofiles', 'GetChats']),
    
    preview(person) {
      var ms=this.messages.filter((c) => c.sender == person.userU && c.reciever==this.CurrentUser.id);
      if(ms.length!=0)
      return ms[ms.length-1].preview+"..."
      else return "No messages"
    },
    select_user(user) {
      this.selected_user = user;
      this.scroll_to_bottom();
      this.is_show_user_menu = false;
    },
    send_message() {
      if (this.text_message.trim()) {
        let user = this.Userprofiles.find((d) => d.userU == this.selected_user.userU);
        this.CreateChat({ message: this.text_message, sender: this.CurrentUser.id, reciever: user.userU, preview: this.text_message.slice(0, 10) });
        this.text_message = '';
        this.scroll_to_bottom();
      }
    },
    scroll_to_bottom() {
      setTimeout(() => {
        document.querySelector('.chat-conversation-box').scrollTo({ left: 0, top: document.querySelector('.chat-conversation-box').scrollHeight, behavior: 'smooth' });
      });
    },
  },
  created: function () {
    this.GetUsers();
    this.GetChats();
    this.GetUserprofiles();
    this.messages = this.Chats;
    
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
        let contact=[]
      for (let c in this.messages.sort(function(a, b){return b-a})){
        if(contact.find((d)=>d==this.messages[c].sender)==null&&this.messages[c].reciever==this.CurrentUser.id){
            contact.push(this.messages[c].sender)
        }
      }
      for(let c in contact){
        for(let u in this.Userprofiles){
        if(this.Userprofiles[u].userU != this.CurrentUser.id && this.Userprofiles[u].userU==contact[c]){
         this.Contactlist.push(this.Userprofiles[u])
        }
        }
      }
      for(let u in this.Userprofiles){
        if(this.Userprofiles[u].userU != this.CurrentUser.id && contact.find((d)=>d==this.Userprofiles[u].userU)==null){
         this.Contactlist.push(this.Userprofiles[u])
        }
        }
        for (let c in this.Chats) {
          if (this.Chats[c].reciever == this.CurrentUser.id) {
            let senderr = this.Chats[c].sender;
            var exists = this.senders.some(function (sender) {
              return sender.id === senderr;
            });
            if (exists == false) {
              for (let p in this.Userprofiles) {
                if (this.Userprofiles[p].userU == this.Chats[c].sender) {
                  this.senders.push(this.Userprofiles[p]);
                }
              }
            }
          }
        }
      }
    }
  },
};
</script>
