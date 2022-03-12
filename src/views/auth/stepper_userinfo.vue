<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Informations</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-lg-12 col-md-12 col-12 layout-spacing">
        <div class="panel br-4">
          <div class="panel-body">
            <form-wizard title="" @on-complete="onComplete" subtitle="" shape="circle" color="#4361ee">
              <tab-content title="More Informations" :before-change="beforeTabSwitch" icon="far fa-user">
                <b-form>
                  <b-form-row class="mb-4">
                    <b-form-group label="First name" class="col-md-4">
                      <b-input type="text" placeholder="First name" v-model="form.firstname" :class="[is_submit_form1 ? (form.firstname ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.firstname }">Please fill the first name</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group label="Last name" class="col-md-4">
                      <b-input type="text" placeholder="Last name" v-model="form.lastname" :class="[is_submit_form1 ? (form.lastname ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.lastname }">Please fill the last name</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group label="Age" class="col-md-4">
                      <b-input type="number" placeholder="Age" v-model="form.age" :class="[is_submit_form1 ? (form.age ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.age }">Please fill the age</b-form-invalid-feedback>
                    </b-form-group>
                  </b-form-row>
                  <hr />
                  <b-form-row class="mb-4">
                    <b-form-group label="Phone Number" class="col-md-6">
                      <MazPhoneNumberInput Black v-model="form.tel" :class="[is_submit_form1 ? (form.tel ? 'is-valid' : 'is-invalid') : '']" />
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.tel }">Please fill the Phone number</b-form-invalid-feedback>
                    </b-form-group>
                  </b-form-row>
                  <hr />
                  <b-form-row class="mb-4">
                    <b-form-group class="col-md-6" label="Address">
                      <b-input placeholder="1234 Main St" v-model="form.address"></b-input>
                    </b-form-group>
                    <b-form-group class="col-md-6" label="Country">
                      <country-select
                        class="country-select"
                        v-model="form.country"
                        :country="form.country"
                        topCountry="US"
                        :class="[is_submit_form1 ? (form.country ? 'is-valid' : 'is-invalid') : '']"
                      />
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.country }">Please fill the Country</b-form-invalid-feedback>
                    </b-form-group>
                  </b-form-row>
                  <hr />
                  <b-form-row class="mb-4">
                    <div class="custom-file-container col-6" data-upload-id="myFirstImage">
                      <label>Upload Image <a href="javascript:void(0)" class="custom-file-container__image-clear" title="Clear Image">x</a></label>
                      <label class="custom-file-container__custom-file">
                        <input type="file" @change="onFileChanged" class="custom-file-container__custom-file__custom-file-input" accept="image/*" />
                        <input type="hidden" name="MAX_FILE_SIZE" value="10485760" />
                        <span class="custom-file-container__custom-file__custom-file-control"></span>
                      </label>
                      <div class="custom-file-container__image-preview"></div>
                    </div>
                  </b-form-row>
                </b-form>
              </tab-content>
              <tab-content title="Preferences" icon="far fa-heart">
                <div class="col-4 pl-4">
                  <h5>Question Category:</h5>
                  <b-select v-model="form.category" value="Default select">
                    <b-select-option value="0">Select Category</b-select-option>
                    <b-select-option v-for="c in Questioncategories" :key="c.id" :value="c.id">{{ c.typeC }}</b-select-option>
                  </b-select>
                </div>
              </tab-content>
            </form-wizard>
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
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
import '@/assets/sass/scrollspyNav.scss';
import { FormWizard, TabContent } from 'vue-form-wizard';
import 'vue-form-wizard/dist/vue-form-wizard.min.css';
import '@/assets/sass/forms/file-upload-with-preview.min.css';
import FileUploadWithPreview from 'file-upload-with-preview';
import '@/assets/sass/font-icons/fontawesome/css/regular.css';
import '@/assets/sass/font-icons/fontawesome/css/fontawesome.css';
export default {
  metaInfo: { title: 'User info' },
  components: {
    FormWizard,
    TabContent,
  },
  data() {
    return {
      form: {
        firstname: '',
        lastname: '',
        age: '',
        address: '',
        tel: '',
        country: '',
        userU: [],
        //pref
        category: 0,
        //role
        roleU: null,
      },
      CurrentUser: [],
      is_submit_form1: false,
      ok: false,
      image: null,
    };
  },
  mounted() {
    new FileUploadWithPreview('myFirstImage', {
      images: {
        baseImage: require('@/assets/images/file-preview.png'),
        backgroundImage: '',
      },
    });
  },
  computed: {
    ...mapGetters({
      Users: 'StateUsers',
      User: 'StateUser',
      Questioncategories: 'StateQuestioncategories',
      Userprofiles: 'StateUserprofiles',
      Roles: 'StateRoles',
      Preferences: 'StatePreferences',
    }),
  },
  methods: {
    ...mapActions(['CreateRole', 'CreatePreference', 'GetPreferences', 'GetRoles', 'GetUsers', 'CreateUserprofile', 'GetUserprofiles', 'GetQuestioncategories']),
    //upload image
    onFileChanged(event) {
      this.image = event.target.files[0];
    },
    beforeTabSwitch: function () {
      for (let u in this.Users) {
        if (this.Users[u].username == this.User) {
          this.form.userU = this.Users[u];
        }
      }
      this.is_submit_form1 = true;
      if (this.form.firstname && this.form.lastname && this.form.age && this.form.country && this.form.tel) {
          for (let r in this.Roles) {
            if (this.Roles[r].userRole == this.form.userU.id) {
              this.form.roleU = this.Roles[r].id;
            }
          }
        var formdata = new FormData();
        if (this.image != null) {
          formdata.append('imageU', this.image);
        }
        formdata.append('lastname', this.form.lastname);
        formdata.append('firstname', this.form.firstname);
        formdata.append('address', this.form.address);
        formdata.append('email', this.form.email);
        formdata.append('age', this.form.age);
        formdata.append('tel', this.form.tel);
        formdata.append('country', this.form.country);
        if (this.form.roleU != null) {
          formdata.append('roleU', this.form.roleU);
        }
        formdata.append('userU', this.form.userU.id);
        //
        for (let u in this.Userprofiles) {
          if (this.Userprofiles[u].userU == this.form.userU.id) {
            axios.put('/userprofile/userprofile-update/' + this.Userprofiles[u].id + '/', formdata);
            this.ok = true;
          }
        }
        if (this.ok == false) {
          console.log(this.form);
          this.CreateUserprofile(formdata);
        }
        return true;
      } else {
        return false;
      }
    },
    onComplete: async function () {
      for (let u in this.Userprofiles) {
        if (this.Userprofiles[u].userU == this.form.userU.id) {
          await this.CreatePreference({ userprofilePref: this.Userprofiles[u].id, categoryPref: this.form.category, brandPref: null });
          console.log(this.Preferences);
          for (let p in this.Preferences) {
            if (this.Preferences[p].userprofilePref == this.Userprofiles[u].id) {
              axios.put('/userprofile/userprofile-update/' + this.Userprofiles[u].id + '/', { preferencesU: this.Preferences[p].id });
            }
          }
        }
      }
      this.$router.push('/questions');
    },
  },

  created() {
    this.GetUsers();
    this.GetQuestioncategories();
    this.GetUserprofiles();
    this.GetRoles();
    this.GetPreferences();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
        for (let u in this.Userprofiles) {
          if (this.Userprofiles[u].userU == this.CurrentUser.id) {
            this.$router.push('/questions');
          }
        }
      }
    }
  },
};
</script>