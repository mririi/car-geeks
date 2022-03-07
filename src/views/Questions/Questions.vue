<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Questions</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>
    <div>
      <div class="row mr-1 float-right">
        <div class="col-lg-12 col-md-12 col-sm-12 filtered-list-search-live mx-auto">
          <b-form class="form-inline my-2 my-lg-0 justify-content-center" @submit.prevent="search">
            <div class="w-100">
              <b-input v-model="search" class="w-100 product-search br-25" placeholder="Search Questions" @keyup="search"></b-input>
            </div>
          </b-form>
        </div>
      </div>

      <div v-b-toggle.collapse-1 class="mt-3 mb-4 col-xl-1">
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
      </div>
      <b-collapse id="collapse-1">
        <b-card class="bg-transparent border-0 border-white w-25 ml-3 default mt-2 mb-4">
          <b-form-group class="" label="Categories : " v-slot="{ ariaDescribedby }">
            <b-form-checkbox-group id="checkbox-group-2" v-model="category" :aria-describedby="ariaDescribedby" name="flavour-a1">
              <div v-for="c in Questioncategories" :key="c.id">
                <b-form-checkbox class="" :value="c.id">
                  {{ c.typeC }}
                </b-form-checkbox>
              </div>
            </b-form-checkbox-group>
          </b-form-group>
        </b-card>
      </b-collapse>
    </div>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-md-12 col-sm-12 col-12 ">
        <div class="panel-body" v-for="q in filterByCategory" :key="q.id">
          <b-card class="component-card_9" v-if="q.accepted == true">
            <div v-if="CurrentUserProfile.id == q.userprofileQ">
              <b-dropdown variant="icon-only" dropleft toggle-tag="a" class="mb-4 mr-2 custom-dropdown float-right">
                <template #button-content>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    style="width: 24px; height: 24px"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="feather feather-more-vertical"
                  >
                    <circle cx="12" cy="12" r="1"></circle>
                    <circle cx="12" cy="5" r="1"></circle>
                    <circle cx="12" cy="19" r="1"></circle>
                  </svg>
                </template>
                <b-dropdown-item :href="'/updatequestion/'+q.id">Modify</b-dropdown-item>
                <b-dropdown-item @click="deleteQuestion(q.id)">Delete</b-dropdown-item>
              </b-dropdown>
            </div>

            <p class="meta-date mb-3">{{ q.dateQ | formatDate }}</p>

            <router-link :to="'questionpage/' + q.id">
              <b-card-title class="ml-4" title-tag="h4">{{ q.titleQ }}</b-card-title></router-link
            >
            <b-card-text class="ml-4">{{ q.contentQ }}</b-card-text>

            <div class="meta-info">
              <div class="meta-user">
                <div v-for="p in Userprofiles" :key="p.id">
                  <div class="avatar avatar-sm" v-if="p.id == q.userprofileQ">
                    <b-avatar :src="'http://127.0.0.1:8000' + p.imageU" class="avatar-title rounded-circle"></b-avatar>
                  </div>
                </div>
                <div v-for="p in Userprofiles" :key="p.id">
                  <div v-if="p.id == q.userprofileQ">
                    <div class="user-name mt-2">{{ p.firstname }} {{ p.lastname }}</div>
                  </div>
                </div>
              </div>
              <div class="meta-action">
                <div class="meta-likes">
                  <svg viewBox="0 0 22 18" width="32" height="28" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
                  <span class="h6 ml-1">{{ q.nblikes }}</span>
                </div>

                <div class="meta-view">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="32" height="28" preserveAspectRatio="xMidYMid meet" viewBox="0 0 14 12">
                    <path
                      fill="currentColor"
                      d="M6.598 5.013a.144.144 0 0 1 .202.134V6.3a.5.5 0 0 0 .5.5c.667 0 2.013.005 3.3.822c.984.624 1.99 1.76 2.595 3.876c-1.02-.983-2.185-1.516-3.205-1.799a8.74 8.74 0 0 0-1.921-.306a7.404 7.404 0 0 0-.798.008h-.013l-.005.001h-.001L7.3 9.9l-.05-.498a.5.5 0 0 0-.45.498v1.153c0 .108-.11.176-.202.134L2.614 8.254a.503.503 0 0 0-.042-.028a.147.147 0 0 1 0-.252a.499.499 0 0 0 .042-.028l3.984-2.933zM7.8 10.386c.068 0 .143.003.223.006c.434.02 1.034.086 1.7.271c1.326.368 2.896 1.202 3.94 3.08a.5.5 0 0 0 .933-.305c-.464-3.71-1.886-5.662-3.46-6.66c-1.245-.79-2.527-.942-3.336-.971v-.66a1.144 1.144 0 0 0-1.767-.96l-3.994 2.94a1.147 1.147 0 0 0 0 1.946l3.994 2.94a1.144 1.144 0 0 0 1.767-.96v-.667z"
                    />
                  </svg>
                  <span class="h6 "> {{ q.nbrep }}</span>
                </div>
              </div>
            </div>
          </b-card>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.layout-px-spacing {
  min-height: calc(100vh - 170px) !important;
}
</style>
<script>
//import '@/assets/sass/elements/search.scss'
import '@/assets/sass/components/cards/card.scss';
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  name: 'Questions',
  components: {},
  data() {
    return {
      search: '',
      category: [],
      CurrentUserProfile: [],
      CurrentUser: [],
    };
  },
  created: function () {
    this.GetQuestions();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    this.GetUsers();
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
        return question.titleQ.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    filterByCategory: function () {
      if (this.category != '') {
        return this.filteredList.filter((question) => this.category.includes(question.categoryQ));
      } else return this.filteredList;
    },
  },
  methods: {
    ...mapActions(['GetQuestions', 'GetUsers', 'GetUserprofiles', 'GetQuestioncategories']),

    deleteQuestion(id) {
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonText: 'Delete',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.delete(`/question/question-delete/${id}/`);
          axios.put('/userprofile/userprofile-update/' + this.CurrentUserProfile.id + '/', {
            nbquestions: (this.CurrentUserProfile.nbquestions -= 1),
          });
          this.$swal('Deleted!', 'Your question has been deleted.', 'success');
          this.$router.go();
        }
      });
     
    },
  },
};
</script>
<style scoped>
.search-box {
  width: fit-content;
  height: fit-content;
  position: relative;
}
.input-search {
  height: 50px;
  width: 50px;
  border-style: none;
  padding: 10px;
  font-size: 18px;
  letter-spacing: 2px;
  outline: none;
  border-radius: 25px;
  transition: all 0.5s ease-in-out;
  background-color: #25c2a0;
  padding-right: 40px;
  color: #fff;
}
.input-search::placeholder {
  color: rgba(255, 255, 255, 0.5);
  font-size: 18px;
  letter-spacing: 2px;
  font-weight: 100;
}
.btn-search {
  width: 50px;
  height: 50px;
  border-style: none;
  font-size: 20px;
  font-weight: bold;
  outline: none;
  cursor: pointer;
  border-radius: 50%;
  position: absolute;
  right: 0px;
  color: #ffffff;
  background-color: transparent;
  pointer-events: painted;
}
.btn-search:focus ~ .input-search {
  width: 400px;
  border-radius: 0px;
  background-color: transparent;
  border-bottom: 1px solid #25c2a0;
  border-radius: 10px;
  transition: all 500ms cubic-bezier(0, 0.11, 0.35, 2);
}
.input-search:focus {
  width: 400px;
  border-radius: 0px;
  background-color: transparent;
  border-bottom: 1px solid #25c2a0;
  border-radius: 10px;
  transition: all 500ms cubic-bezier(0, 0.11, 0.35, 2);
}
</style>