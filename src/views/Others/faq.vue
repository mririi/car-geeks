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
                    <li class="list-unstyled">
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
                      What can i do to get my question accepted
                    </li>
                    <li class="list-unstyled">
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
                      How can i add service
                    </li>
                    <li class="list-unstyled">
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
                      How can i add my company
                    </li>
                  </ul>
                </div>
                <div class="col-md-6">
                  <ul class="">
                    <li class="list-unstyled">
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
                      How to create a group
                    </li>
                    <li class="list-unstyled">
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
                      How to contact administration
                    </li>
                    <li class="list-unstyled">
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
                      How to navigate
                    </li>
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
                <b-card no-body v-for="q in Questions" :key="q.id">
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
                      <router-link :to="'/questionpage/'+q.id">
                      <span class="faq-q-title ml-3">{{q.titleQ}}</span>
                      
                      <div class="like-faq">
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
                          class="feather feather-thumbs-up"
                        >
                          <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
                        </svg>
                        <span class="faq-like-count">{{q.nblikes}}</span>
                      </div>
                      </router-link>
                    </div>
                  </b-card-header>
                  <b-collapse id="fqcollapseOne" accordion="faq-accordion">
                    <b-card-body v-for="r in Replies" :key="r.id">
                        <span v-if="r.questionRep == q.id && r.checked==true">
                      <p>
                        {{r.contentR}}
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
  created:function(){
      this.GetQuestions()
      this.GetReplies()
  },
  computed:{
      ...mapGetters({
     Questions:'StateQuestions',
     Replies:'StateReplies'
    }),
    /*filteredList() {
      return this.Questions.filter((quest) => {
        return quest.nblikes.sort((a, b) => b-a)
      });
    },*/
  },
  methods: {
      ...mapActions(['GetQuestions','GetReplies']),
  },
};
</script>
