<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Replies</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div id="tableHover" class="col-lg-12 col-12 layout-spacing mt-5">
      <div class="statbox panel box box-shadow">
        <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 mt-3 filtered-list-search layout-spacing align-self-center">
          <form class="form-inline my-2 my-lg-0">
            <div class="">
              <b-input v-model.trim="search" class="product-search" placeholder="Search Replies..." />
             
            </div>
          </form>
        </div>

        <div class="panel-body">
          <b-table responsive bordered hover :items="filteredList" :fields="fields">
            <template #cell(accepted)="data">
              <span v-if="data.item.accepted == true">
                <b-badge variant="success">Accepted</b-badge>
              </span>
              <span v-else>
                <b-badge variant="danger">Pending</b-badge>
              </span>
            </template>
            <template #cell(dateR)="data">
               {{data.item.dateR |formatDate}}
            </template>
            <template #cell(userprofileRep)="data">
              <span v-for="u in Userprofiles" :key="u.id">
                <span v-if="u.id == data.item.userprofileRep">
                   {{u.firstname}} {{u.lastname}}
                </span>
              </span>
            </template>
             <template #cell(questionRep)="data">
              <span v-for="q in Questions" :key="q.id">
                <span v-if="q.id == data.item.questionRep">
                    <router-link :to="'/questionpage/'+q.id">
                   {{q.titleQ}}
                    </router-link>
                </span>
              </span>
            </template>
            <template #cell(imageR)="data">
                <span v-if="data.item.imageR!=null">
              <b-avatar :src="'http://127.0.0.1:8000'+data.item.imageR" size="4rem" rounded="lg"  alt="" srcset=""/>
              </span>
              <span v-else>
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="4em" height="4em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64"><path fill="currentColor" d="M32 2C15.432 2 2 15.432 2 32.001C2 48.567 15.432 62 32 62s30-13.433 30-29.999C62 15.432 48.568 2 32 2zm22 30.001c0 4.629-1.433 8.922-3.876 12.465l-30.591-30.59A21.889 21.889 0 0 1 32 10c12.15 0 22 9.851 22 22.001zm-44 0a21.9 21.9 0 0 1 3.876-12.468l30.591 30.591A21.887 21.887 0 0 1 32 54.001c-12.15 0-22-9.852-22-22z"/></svg>
              </span>
            </template>
            <template #cell(actions)="data">
              <span @click="Accept(data.item.id,data.item.userprofileRep)">
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
                  class="feather feather-check-circle text-primary ac"
                >
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22 4 12 14.01 9 11.01"></polyline>
                </svg>
              </span>
            </template>
          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.table3 .actions svg {
  padding: 2px;
}
.ac{
    cursor: pointer;
}
</style>
<script>
import '@/assets/sass/apps/contacts.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios'
export default {
  metaInfo: { title: 'Bootstrap Custom Table' },
  data() {
    return {
      category: [],
      CurrentUserProfile: [],
      items: [
        {
          title: '',
          date: '',
          category: '',
          replies: '',
          user: '',
          status: '',
        },
      ],
      search: '',
      CurrentUser: [],
      fields: [
        { key: 'imageR', label: 'Image' ,class: 'text-center ' },
        { key: 'contentR', label: 'Content' },
        { key: 'dateR', label: 'Date' },
        { key: 'nblikesR', label: 'Likes' },
        { key: 'nbCommentR', label: 'Comments' },
        { key: 'questionRep', label: 'Question'},
        { key: 'userprofileRep', label: 'User' },
        { key: 'accepted', label: 'Status', class: 'text-center' },
        { key: 'actions', label: 'Actions', class: 'text-center  ' },
      ],
    };
  },

  methods: {
    ...mapActions(['GetQuestions','GetReplies', 'GetUsers', 'GetUserprofiles', 'GetQuestioncategories']),
    async Accept(id,userid) {
      await axios.post('/reply/reply-update/' + id + '/', { accepted: true });
       for(let u in this.Userprofiles)
      {
          if(this.Userprofiles[u].id==userid)
          {
           await axios.put('/userprofile/userprofile-update/' + userid + '/', { nbreplies:this.Userprofiles[u].nbreplies+=1  });
          }
      }
      
      this.$router.go();
    },
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Userprofiles: 'StateUserprofiles',
      Questioncategories: 'StateQuestioncategories',
      User: 'StateUser',
      Users: 'StateUsers',
      Replies:'StateReplies'
    }),

    filteredList() {
      return this.Replies.filter((rep) => {
        return rep.contentR.toLowerCase().includes(this.search.toLowerCase())&& rep.accepted==false;
      });
    },
    
  },
  created: function () {
    this.GetQuestions();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    this.GetUsers();
    this.GetReplies();
    /*for (let q in this.Questions) {
     this.items[q].title = this.Questions[q].titleQ;
      this.items[q].date = this.Questions[q].dateQ;
      for (let c in this.Questioncategories) {
        if (this.Questioncategories[c].id == this.Questions[q].categoryQ) {
          this.items[q].category = this.Questioncategories[c].typeC;
        }
      }
      this.items[q].replies = this.Questions[q].nbrep;
      for (let u in this.Userprofiles) {
        if (this.Userprofiles[u].id == this.Questions[q].userprofileQ) {
          this.items[q].user = this.Userprofiles[u].firstname + ' ' + this.Userprofiles[u].lastname;
        }
      }
      this.items[q].status = this.Questions[q].accepted;
    }*/

    console.log(this.items);
    console.log(this.Questions);
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
      }
    }
  },
};
</script>
