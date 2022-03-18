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
              <span v-b-toggle.collapse-1 class="ml-2 mt-2 justify-content-end">
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
                        <b-form-checkbox :value="c.id">
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
          <b-table responsive bordered hover :items="filterByCategory" :fields="fields">
            <template #cell(accepted)>
              <span>
                <b-badge variant="danger">Pending</b-badge>
              </span>
            </template>
            <template #cell(dateQ)="data">
              {{ data.item.dateQ | formatDate }}
            </template>
            <template #cell(userprofileQ)="data">
              <span v-for="u in Userprofiles" :key="u.id">
                <span v-if="u.id == data.item.userprofileQ"> {{ u.firstname }} {{ u.lastname }} </span>
              </span>
            </template>
            <template #cell(categoryQ)="data">
              <span v-for="c in Questioncategories" :key="c.id">
                <span v-if="c.id == data.item.categoryQ">
                  {{ c.typeC }}
                </span>
              </span>
            </template>
            <template #cell(actions)="data">
              <span @click="Accept(data.item.id,data.item.userprofileQ)">
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
            <template #cell(imageQ)="data">
              <span v-if="data.item.imageQ != null">
                <b-avatar :src="'http://127.0.0.1:8000' + data.item.imageQ" size="4rem" rounded="lg" alt="" srcset="" />
              </span>
              <span v-else>
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="4em" height="4em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64">
                  <path
                    fill="currentColor"
                    d="M32 2C15.432 2 2 15.432 2 32.001C2 48.567 15.432 62 32 62s30-13.433 30-29.999C62 15.432 48.568 2 32 2zm22 30.001c0 4.629-1.433 8.922-3.876 12.465l-30.591-30.59A21.889 21.889 0 0 1 32 10c12.15 0 22 9.851 22 22.001zm-44 0a21.9 21.9 0 0 1 3.876-12.468l30.591 30.591A21.887 21.887 0 0 1 32 54.001c-12.15 0-22-9.852-22-22z"
                  />
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
.ac {
  cursor: pointer;
}
</style>
<script>
import '@/assets/sass/apps/contacts.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
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
        { key: 'imageQ', label: 'Image', class: 'text-center  ' },
        { key: 'titleQ', label: 'Title' },
        { key: 'contentQ', label: 'Content' },
        { key: 'dateQ', label: 'Date' },
        { key: 'categoryQ', label: 'Category' },
        { key: 'nbrep', label: 'Replies' },
        { key: 'userprofileQ', label: 'User' },
        { key: 'accepted', label: 'Status', class: 'text-center  ' },
        { key: 'actions', label: 'Actions', class: 'text-center  ' },
      ],
    };
  },

  methods: {
    ...mapActions(['GetQuestions', 'GetUsers', 'GetUserprofiles', 'GetQuestioncategories']),
    async Accept(id , userid) {
      await axios.put('/question/question-update/' + id + '/', { accepted: true });
      for(let u in this.Userprofiles)
      {
          if(this.Userprofiles[u].id==userid)
          {
           await axios.put('/userprofile/userprofile-update/' + userid + '/', { nbquestions:this.Userprofiles[u].nbquestions+=1  });
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
    }),

    filteredList() {
      return this.Questions.filter((question) => {
        return question.titleQ.toLowerCase().includes(this.search.toLowerCase()) && question.accepted == false;
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
