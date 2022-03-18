<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Comments</span></li>
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
              <b-input v-model.trim="search" class="product-search" placeholder="Search Comments..." />
             
            </div>
          </form>
        </div>

        <div class="panel-body">
          <b-table responsive bordered hover :items="filteredList" :fields="fields">
           
            <template #cell(dateCo)="data">
               {{data.item.dateCo |formatDate}}
            </template>
            <template #cell(userprofileCo)="data">
              <span v-for="u in Userprofiles" :key="u.id">
                <span v-if="u.id == data.item.userprofileCo">
                   {{u.firstname}} {{u.lastname}}
                </span>
              </span>
            </template>
            <template #cell(replyCo)="data">
              <span v-for="r in Replies" :key="r.id">
                <span v-if="r.id == data.item.replyCo"> 
                   {{r.contentR}}
                </span>
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
</style>
<script>
import '@/assets/sass/apps/contacts.scss';
import { mapGetters, mapActions } from 'vuex';
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
        { key: 'contentCo', label: 'Content' },
        { key: 'dateCo', label: 'Date' },
        { key: 'userprofileCo', label: 'User' },
        { key: 'replyCo', label: 'Reply'},
      ],
    };
  },

  methods: {
    ...mapActions(['GetQuestions','GetReplies', 'GetComments', 'GetUsers', 'GetUserprofiles', 'GetQuestioncategories']),
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Userprofiles: 'StateUserprofiles',
      Questioncategories: 'StateQuestioncategories',
      User: 'StateUser',
      Users: 'StateUsers',
      Replies:'StateReplies',
      Comments:'StateComments'
    }),

    filteredList() {
      return this.Comments.filter((com) => {
        return com.contentCo.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    
  },
  created: function () {
    this.GetQuestions();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    this.GetUsers();
    this.GetReplies();
    this.GetComments();
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
