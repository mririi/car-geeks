<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Questions</span></li>
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
              
              <b-input v-model.trim="search" class="product-search" placeholder="Search Questions..." />
              <span v-b-toggle.collapse-1 class="  ml-2 mt-2 justify-content-end">
        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="22" height="20" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36">
          <path
            fill="currentColor"
            d="M22 33V19.5L33.47 8A1.81 1.81 0 0 0 34 6.7V5a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v1.67a1.79 1.79 0 0 0 .53 1.27L14 19.58v10.2Z"
            class="clr-i-solid clr-i-solid-path-1"
          />
          <path
            fill="currentColor"
            d="M33.48 4h-31a.52.52 0 0 0-.48.52v1.72a1.33 1.33 0 0 0 .39.95l12 12v10l7.25 3.61V19.17l12-12a1.35 1.35 0 0 0 .36-.91V4.52a.52.52 0 0 0-.52-.52Z"
            class="clr-i-solid clr-i-solid-path-1"
          />
          <path fill="none" d="M0 0h36v36H0z" />
        </svg>
        <span class="h6">Filter</span>
              </span>
      <b-collapse id="collapse-1">
        <b-card class="bg-transparent border-0 border-white w-50 ml-3 default mt-2 mb-4">
          <b-form-group label="Categories : " v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group id="checkbox-group-2" v-model="category" :aria-describedby="ariaDescribedby" name="flavour-a1">
              <div v-for="c in Questioncategories" :key="c.id">
                <b-form-checkbox  :value="c.id">
                  {{ c.typeC }}
                </b-form-checkbox>
              </div>
            </b-form-checkbox-group>
          </b-form-group>
        </b-card>
      </b-collapse>
            </div>
          </form>
        </div>
        
   
        <div class="panel-body">
          <b-table responsive bordered hover :items="items" :fields="fields">
          <template #cell(status)="data">
                                <b-badge variant="success">{{data.item.status1}}</b-badge>
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
      items:[{
        title:'',
        date:'',
        category:'',
        replies:'',
        user:'',
        status1:'',
      }],
      search:'',
      CurrentUser: [],
      fields: [{ key: 'title', label: 'Title'} ,{ key: 'date', label: 'Date'}, { key: 'category', label: 'Category'}, { key: 'replies', label: 'Replies'}, { key: 'user', label: 'User'},  { key: 'status', label: 'Status', class: 'text-center  ' }],
    };
  },

  methods: {
    ...mapActions(['GetQuestions', 'GetUsers', 'GetUserprofiles', 'GetQuestioncategories']),
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Userprofiles: 'StateUserprofiles',
      Questioncategories: 'StateQuestioncategories',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    filterByAccepted() {
      
        return this.Questions.filter((question) => {return question.accepted==true});
      
    },
    filteredList() {
      return this.Questions.filter((question) => {
        return question.titleQ.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    filterByCategory: function () {
      if (this.category != '') {
        return this.filteredList.filter((question) => this.category.includes(question.categoryQ));
      } else return this.filteredList;
    },
  },
  created: function () {
    this.GetQuestions();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    this.GetUsers();
    for(let q in this.filterByAccepted){
      this.items[q].title=this.filterByAccepted[q].titleQ
      this.items[q].date=this.filterByAccepted[q].dateQ
      for(let c in this.Questioncategories){
        if(this.Questioncategories[c].id==this.filterByAccepted[q].categoryQ){
          this.items[q].category=this.Questioncategories[c].typeC
        }
      }
      this.items[q].replies=this.filterByAccepted[q].nbrep
      for(let u in this.Userprofiles){
        if(this.Userprofiles[u].id==this.filterByAccepted[q].userprofileQ){
          this.items[q].user=this.Userprofiles[u].firstname+' '+this.Userprofiles[u].lastname
        }
      }
      this.items[q].status1="Accepted"

    }
    console.log(this.items)
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
