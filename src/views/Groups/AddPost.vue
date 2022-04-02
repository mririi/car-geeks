<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Add Post</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-md-12 col-sm-12 col-12">
        <div class="panel-body">
          <div class="row">
            <div id="flRegistrationForm" class="col-lg-12 layout-spacing">
              <div class="statbox panel box box-shadow">
                <div class="panel-heading">
                  <div class="row">
                    <div class="col-xl-10 col-md-12 col-sm-12 col-12">
                      <h4>Add Post</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form novalidate @submit.prevent="submit">
                    <label>Post details <span style="color: red">*</span></label>
                    <b-form-group class="mb-3">
                      <b-textarea
                        rows="4"
                        type="text"
                        v-model="form.detailsP"
                        placeholder="Post details"
                        :class="[is_submit_form1 ? (form.detailsP && form.detailsP.length < 500 && form.detailsP.length > 15 ? 'is-valid' : 'is-invalid') : '']"
                      ></b-textarea>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.detailsP }">Please Enter details between 15 and 500 characters</b-form-invalid-feedback>
                    </b-form-group>
                    <label>Insert image</label>
                    <div class="mb-4">
                      <b-file @change="onFileChanged"></b-file>
                    </div>

                    <!--      <vue-tags-input
      v-model="tag"
      :tags="tags"
      @tags-changed="newTags => tags = newTags"
    />-->
                    <small id="emailHelp2" class="form-text text-muted mt-3"><span style="color: red">*</span> Required Fields</small>
                    <b-button @click="submit" variant="primary" class="mt-4 justfiy-content-end">Submit</b-button>
                  </b-form>
                </div>
              </div>
            </div>
          </div>
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
import '@/assets/sass/components/cards/card.scss';
import '@/assets/sass/forms/file-upload-with-preview.min.css';
import { mapGetters, mapActions } from 'vuex';
//import VueTagsInput from '@johmun/vue-tags-input';
import axios from 'axios';
export default {
  metaInfo: { title: 'Add Post' },
  components: {
    // VueTagsInput,
  },
  data() {
    return {
      
      form: {
        detailsP: '',
      },
      image: null,
      uentreprise: [],
      uprofile: [],
      CurrentUser: [],
      CurrentUserProfile: [],
      is_submit_form1: false,
      group:[]
    };
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();
    this.GetGroups();
    this.GetGroupposts();
     axios.get('/group/group-detail/' + this.$route.params.id + '/').then((response) => {
      this.group = response.data;
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
      }
    }})
  },
  methods: {
    onFileChanged(event) {
      this.image = event.target.files[0];
    },
    ...mapActions(['CreateNotification', 'GetUsers', 'GetUserprofiles', 'GetGroups','GetGroupposts' ,'CreateGrouppost']),
    async submit() {
      try {
        this.is_submit_form1 = true;
        if (
          this.form.detailsP.length < 500 &&
          this.form.detailsP.length > 15
        ) {
          var formdata = new FormData();
          if (this.image != null) {
            formdata.append('imagePost', this.image);
          }
          formdata.append('detailsP', this.form.detailsP);
         /* if (this.CurrentUser.is_superuser) {
            formdata.append('accepted', true);
            axios.put('/userprofile/userprofile-update/' + this.form.userprofileQ + '/', { nbquestions: this.uprofile.nbquestions + 1 });
          }*/
          //formdata.append("tags", this.tags.text);
          formdata.append('userprofilePost', this.CurrentUserProfile.id);
          formdata.append('groupPost', this.$route.params.id);
          if(this.group.userprofileG==this.CurrentUserProfile.id)
          {
            formdata.append('accepted', true);
          }
          await this.CreateGrouppost(formdata);
          
        /*  if (this.CurrentUser.is_superuser == false) {
            await this.CreateNotification({
              message: ' requested a Verification on their question !',
              byuserprofileNo: this.form.userprofileQ,
              byuserentrepriseNo: this.form.userentrepriseQ,
              questionNo: 1,
              foradmin: true,
            });
            this.$swal('Good Job!', 'Your question has been created successfuly, Please wait for the administator to accept it !', 'success');
          }*/
          this.$router.push('/groups');
        }
      } catch (error) {
        throw 'Il ya un error!';
      }
    },
  },
  computed: {
    ...mapGetters({ Userentreprises: 'StateUserentreprises', Questioncategories: 'StateQuestioncategories', Userprofiles: 'StateUserprofiles', User: 'StateUser', Users: 'StateUsers' }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>