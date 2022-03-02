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
                        
                            <form-wizard title="" @on-complete="onComplete" subtitle=""  class="circle" 
                            
                            error-color="#e74c3c"
                            color="#4361ee">
                                <h4 class="text-center mt-2 mb-3">More Informations</h4>
                                <tab-content title="" icon="far fa-user">
                                    <b-form novalidate>
    <b-form-row class="mb-4">
        <b-form-group label="First name" class="col-md-4 ">
            <b-input type="text" placeholder="First name" v-model="form.firstname"  :class="[is_submit_form1 ? (form.firstname ? 'is-valid' : 'is-invalid') : '']"></b-input>
            <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
            <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.firstname}">Please fill the first name</b-form-invalid-feedback>
        </b-form-group>
        <b-form-group label="Last name" class="col-md-4 ">
            <b-input type="text" placeholder="Last name" v-model="form.lastname"  :class="[is_submit_form1 ? (form.lastname ? 'is-valid' : 'is-invalid') : '']"></b-input>
            <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
            <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.lastname}">Please fill the last name</b-form-invalid-feedback>
        </b-form-group>
        <b-form-group label="Age" class="col-md-4 " >
            <b-input type="number" placeholder="Age" v-model="form.age" :class="[is_submit_form1 ? (form.age ? 'is-valid' : 'is-invalid') : '']"></b-input>
            <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
            <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.age}">Please fill the age</b-form-invalid-feedback>
        </b-form-group>
    </b-form-row>
    <b-form-row class="mb-4">
    <b-form-group label="Email" class="col-md-6" >
            <b-input  placeholder="Email@email.com" type="email" v-model="form.email" :class="[is_submit_form1 ? (form.email && email_validate(form.email) ? 'is-valid' : 'is-invalid') : '']"></b-input>
        <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
        <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.email}">Please fill the email</b-form-invalid-feedback>
        </b-form-group>
        <b-form-group label="Phone Number" class="col-md-6">
            <b-input type="number" placeholder="Phone Number" v-model="form.phone" :class="[is_submit_form1 ? (form.phone ? 'is-valid' : 'is-invalid') : '']"></b-input>
            <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
            <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.phone}">Please fill the phone</b-form-invalid-feedback>
        </b-form-group>
    </b-form-row>
    <b-form-row class="mb-4">
      <b-form-group class="col-md-6" label="Address">
        <b-input placeholder="1234 Main St" v-model="form.address" :class="[is_submit_form1 ? (form.address ? 'is-valid' : 'is-invalid') : '']"></b-input>
    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
    <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.address}">Please fill the Address</b-form-invalid-feedback>
    </b-form-group>  
     <b-form-group class="col-md-6" label="Country">
        <b-input placeholder="Your country here" v-model="form.country" :class="[is_submit_form1 ? (form.country ? 'is-valid' : 'is-invalid') : '']"></b-input>
        <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
        <b-form-invalid-feedback :class="{'d-block' : is_submit_form1 && !form.country}">Please fill the Country</b-form-invalid-feedback>
    </b-form-group> 
    </b-form-row>
    <b-form-row class="mb-4">
        <div class="custom-file-container" data-upload-id="myFirstImage">
                                <label>Upload (Single File) <a href="javascript:void(0)" class="custom-file-container__image-clear" title="Clear Image">x</a></label>
                                <label class="custom-file-container__custom-file">
                                    <input type="file" class="custom-file-container__custom-file__custom-file-input" accept="image/*">
                                    <input type="hidden" name="MAX_FILE_SIZE" value="10485760" />
                                    <span class="custom-file-container__custom-file__custom-file-control"></span>
                                </label>
                                <div class="custom-file-container__image-preview"></div>
                            </div>
    </b-form-row>

</b-form>
                                </tab-content>
                                    <b-select value="Default select">
    <b-select-option value="Default select">Default select</b-select-option>
    <b-select-option value="One">One</b-select-option>
    <b-select-option value="Two">Two</b-select-option>
    <b-select-option value="Three">Three</b-select-option>
</b-select>
                            
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
import '@/assets/sass/scrollspyNav.scss';

    import { FormWizard, TabContent } from 'vue-form-wizard';
    import 'vue-form-wizard/dist/vue-form-wizard.min.css';
    import '@/assets/sass/forms/file-upload-with-preview.min.css';
    import FileUploadWithPreview from "file-upload-with-preview";
    import '@/assets/sass/font-icons/fontawesome/css/regular.css';
    import '@/assets/sass/font-icons/fontawesome/css/fontawesome.css';
    export default {
        metaInfo: { title: 'User info' },
        components: {
            FormWizard,
            TabContent,
        },
        data(){
            return{
            form:{
                firstname:'',
                lasttname:'',
                age:'',
                email:'',
                address:'',
                phone:'',
                country:'',
            },
            is_submit_form1: false,
            count: 0
            }
        },
        mounted() {
            new FileUploadWithPreview('myFirstImage', {
                images: {
                    baseImage: require('@/assets/images/file-preview.png'),
                    backgroundImage:''
                },
            });
        },
        methods: {
          onComplete: function(){
      this.submit_form1()
   },
   submit_form1() {
                this.is_submit_form1 = true;
                if (this.form.firstname && this.form.lastname && this.form.age && this.form.address && this.form.email && this.form.country && this.form.phone) {
                    //form validated success
                    this.$bvToast.toast('Form submitted successfully.', { headerClass: 'd-none', bodyClass: 'toast-success', toaster: 'b-toaster-top-center', autohidedelay: 2000 })
                }
            },
            email_validate(email) {
                const regexp = /^[\w.%+-]+@[\w.-]+\.[\w]{2,6}$/;
                return regexp.test(email);
            },
     
    },
    };
</script>
