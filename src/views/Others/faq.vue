<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                
                <li class="breadcrumb-item active" aria-current="page"><span>FAQ</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="fq-header-wrapper">
      <div class="container">
        <div class="row">
          <div class="col-md-6 align-self-center order-md-0 order-1">
            <h1 class="">FAQ</h1>
            <p class="">Get Instant Answer From Popular Question Asked By Other Users</p>
          </div>
          <div class="col-md-6 order-md-0 order-0">
            <div class="banner-img">
              <img src="@/assets/images/faq.svg" class="d-block" alt="header-image" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="faq container">
      <div class="faq-layouting layout-spacing">
        <div class="fq-comman-question-wrapper">
          <div class="row">
            <div class="col-md-12">
              <h3>Some common questions</h3>
              <div class="row">
                <div class="col-md-6">
                  <ul class="">
                    <span v-for="q in filteredList.slice(0,3)" :key="q.id">
                      <router-link :to="'/questionpage/'+q.id+'/'+q.slug">
                    <li   class="list-unstyled">
                      <div class="icon-svg">
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
                          class="feather feather-check"
                        >
                          <polyline points="20 6 9 17 4 12"></polyline>
                        </svg>
                      </div>
                      {{q.titleQ}}
                    </li>
                    </router-link>
                    </span>
                  </ul>
                </div>
                <div class="col-md-6">
                  <ul class="">
                    <span v-for="q in filteredList.slice(3,6)" :key="q.id">
                      <router-link :to="'/questionpage/'+q.id+'/'+q.slug">
                    <li  class="list-unstyled">
                      <div class="icon-svg">
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
                          class="feather feather-check"
                        >
                          <polyline points="20 6 9 17 4 12"></polyline>
                        </svg>
                      </div>
                      {{q.titleQ}}
                    </li>
                    </router-link>
                    </span>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="fq-tab-section">
          <div class="row">
            <div class="col-md-12 mb-5 mt-5">
              <h2>Platform Base Questions</h2>

              <div class="accordion" id="faq">
                <b-card no-body>
                  <b-card-header role="tab">
                    <div class="mb-0" v-b-toggle.fqcollapseOne>
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <path
                          fill="currentColor"
                          d="m20.772 10.156l-1.368-4.105A2.995 2.995 0 0 0 16.559 4H7.441a2.995 2.995 0 0 0-2.845 2.051l-1.368 4.105A2.003 2.003 0 0 0 2 12v5c0 .753.423 1.402 1.039 1.743c-.013.066-.039.126-.039.195V21a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2h12v2a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2.062c0-.069-.026-.13-.039-.195A1.993 1.993 0 0 0 22 17v-5c0-.829-.508-1.541-1.228-1.844zM4 17v-5h16l.002 5H4zM7.441 6h9.117c.431 0 .813.274.949.684L18.613 10H5.387l1.105-3.316A1 1 0 0 1 7.441 6z"
                        />
                        <circle cx="6.5" cy="14.5" r="1.5" fill="currentColor" />
                        <circle cx="17.5" cy="14.5" r="1.5" fill="currentColor" />
                      </svg>
                      <span class="faq-q-title ml-3">What can i do to get my question accepted ?</span>
                    </div>
                  </b-card-header>
                  <b-collapse id="fqcollapseOne" accordion="faq-accordion">
                    <b-card-body >
                        <span >
                      <p class="ml-5">
                       To get your question accepted, you must ask a good and detailed question and it shouldn't be asked before without bad language or racist words then wait for the admin to accept it.
                      </p>
                      </span>
                    </b-card-body>
                  </b-collapse>
                </b-card>

                
              </div>
              <div class="accordion" id="faq">
                <b-card no-body>
                  <b-card-header role="tab">
                    <div class="mb-0" v-b-toggle.fqcollapseTwo>
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <path
                          fill="currentColor"
                          d="m20.772 10.156l-1.368-4.105A2.995 2.995 0 0 0 16.559 4H7.441a2.995 2.995 0 0 0-2.845 2.051l-1.368 4.105A2.003 2.003 0 0 0 2 12v5c0 .753.423 1.402 1.039 1.743c-.013.066-.039.126-.039.195V21a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2h12v2a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2.062c0-.069-.026-.13-.039-.195A1.993 1.993 0 0 0 22 17v-5c0-.829-.508-1.541-1.228-1.844zM4 17v-5h16l.002 5H4zM7.441 6h9.117c.431 0 .813.274.949.684L18.613 10H5.387l1.105-3.316A1 1 0 0 1 7.441 6z"
                        />
                        <circle cx="6.5" cy="14.5" r="1.5" fill="currentColor" />
                        <circle cx="17.5" cy="14.5" r="1.5" fill="currentColor" />
                      </svg>
                      <span class="faq-q-title ml-3">How can i add service ?</span>
                    </div>
                  </b-card-header>
                  <b-collapse id="fqcollapseTwo" accordion="faq-accordion">
                    <b-card-body >
                        <span >
                      <p class="ml-5">
                       To create service, first you have to be verified (you can do that by clicking on the 'Get Verified' Button if you are logged in as a normal user)
                       Once you are verified, then you can click on the button named 'Add Service' located in the right sidebar in the list services page .
                      </p>
                      </span>
                    </b-card-body>
                  </b-collapse>
                </b-card>

                
              </div>
              <div class="accordion" id="faq">
                <b-card no-body>
                  <b-card-header role="tab">
                    <div class="mb-0" v-b-toggle.fqcollapseThree>
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <path
                          fill="currentColor"
                          d="m20.772 10.156l-1.368-4.105A2.995 2.995 0 0 0 16.559 4H7.441a2.995 2.995 0 0 0-2.845 2.051l-1.368 4.105A2.003 2.003 0 0 0 2 12v5c0 .753.423 1.402 1.039 1.743c-.013.066-.039.126-.039.195V21a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2h12v2a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2.062c0-.069-.026-.13-.039-.195A1.993 1.993 0 0 0 22 17v-5c0-.829-.508-1.541-1.228-1.844zM4 17v-5h16l.002 5H4zM7.441 6h9.117c.431 0 .813.274.949.684L18.613 10H5.387l1.105-3.316A1 1 0 0 1 7.441 6z"
                        />
                        <circle cx="6.5" cy="14.5" r="1.5" fill="currentColor" />
                        <circle cx="17.5" cy="14.5" r="1.5" fill="currentColor" />
                      </svg>
                      <span class="faq-q-title ml-3">How can i create a professional account ?</span>
                    </div>
                  </b-card-header>
                  <b-collapse id="fqcollapseThree" accordion="faq-accordion">
                    <b-card-body >
                        <span >
                      <p class="ml-5">
                       You can create a professional account simply by going to the register page and clicking the 'I am an entreprise' Checkbox then Clicking on the button 'Get Started' and follow the steps.
                      </p>
                      </span>
                    </b-card-body>
                  </b-collapse>
                </b-card>
              </div>
              <div class="accordion" id="faq">
                <b-card no-body>
                  <b-card-header role="tab">
                    <div class="mb-0" v-b-toggle.fqcollapseFour>
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <path
                          fill="currentColor"
                          d="m20.772 10.156l-1.368-4.105A2.995 2.995 0 0 0 16.559 4H7.441a2.995 2.995 0 0 0-2.845 2.051l-1.368 4.105A2.003 2.003 0 0 0 2 12v5c0 .753.423 1.402 1.039 1.743c-.013.066-.039.126-.039.195V21a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2h12v2a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2.062c0-.069-.026-.13-.039-.195A1.993 1.993 0 0 0 22 17v-5c0-.829-.508-1.541-1.228-1.844zM4 17v-5h16l.002 5H4zM7.441 6h9.117c.431 0 .813.274.949.684L18.613 10H5.387l1.105-3.316A1 1 0 0 1 7.441 6z"
                        />
                        <circle cx="6.5" cy="14.5" r="1.5" fill="currentColor" />
                        <circle cx="17.5" cy="14.5" r="1.5" fill="currentColor" />
                      </svg>
                      <span class="faq-q-title ml-3">How to create a group ?</span>
                    </div>
                  </b-card-header>
                  <b-collapse id="fqcollapseFour" accordion="faq-accordion">
                    <b-card-body >
                        <span >
                      <p class="ml-5">
                       To create group, you have to click on 'Groups' in the left sidebar then click on the button named 'Create Group' located in the right sidebar or press <router-link to="creategroup" class="text-info">here</router-link> to access the page directly.
                      </p>
                      </span>
                    </b-card-body>
                  </b-collapse>
                </b-card>
              </div>
              <div class="accordion" id="faq">
                <b-card no-body>
                  <b-card-header role="tab">
                    <div class="mb-0" v-b-toggle.fqcollapseFive>
                      <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                        <path
                          fill="currentColor"
                          d="m20.772 10.156l-1.368-4.105A2.995 2.995 0 0 0 16.559 4H7.441a2.995 2.995 0 0 0-2.845 2.051l-1.368 4.105A2.003 2.003 0 0 0 2 12v5c0 .753.423 1.402 1.039 1.743c-.013.066-.039.126-.039.195V21a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2h12v2a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-2.062c0-.069-.026-.13-.039-.195A1.993 1.993 0 0 0 22 17v-5c0-.829-.508-1.541-1.228-1.844zM4 17v-5h16l.002 5H4zM7.441 6h9.117c.431 0 .813.274.949.684L18.613 10H5.387l1.105-3.316A1 1 0 0 1 7.441 6z"
                        />
                        <circle cx="6.5" cy="14.5" r="1.5" fill="currentColor" />
                        <circle cx="17.5" cy="14.5" r="1.5" fill="currentColor" />
                      </svg>
                      <span class="faq-q-title ml-3">How to contact administration ?</span>
                    </div>
                  </b-card-header>
                  <b-collapse id="fqcollapseFive" accordion="faq-accordion">
                    <b-card-body >
                        <span >
                      <p class="ml-5">
                       You can find the contact section in the left sidebar by clicking on the Contact-Us link or <router-link to="contact-us" class="text-info">here</router-link>.
                      </p>
                      </span>
                    </b-card-body>
                  </b-collapse>
                </b-card>

                
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@/assets/sass/pages/faq/faq.scss';
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'FAQ' },
  mounted() {},
  data(){
    return{
      mostliked:[],
    }
  },
  created:function(){
      this.GetQuestions()
      this.GetReplies()
      this.mostliked = this.Questions.sort((a, b) => b.nblikes - a.nblikes);
  },
  computed:{
      ...mapGetters({
     Questions:'StateQuestions',
     Replies:'StateReplies'
    }),
    filteredList() {
      return this.mostliked.filter((quest) => {
        return quest.accepted==true
      });
    },
  },
  methods: {
      ...mapActions(['GetQuestions','GetReplies']),
  },
};
</script>
