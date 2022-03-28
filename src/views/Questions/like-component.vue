<template>
    <span v-if="userprofile!=null || userentreprise!=null">
    <span v-if="liked==true">
        <svg @click="likedreply()" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
      <path
        fill="currentColor"
        d="M128 447.1v-224c0-17.67-14.33-31.1-32-31.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.7 1.8 32-11.7 32-30.2zm384-223c0-26.5-21.48-47.98-48-47.98H317.5c22.77-37.91 34.52-80.88 34.52-96.02C352 56.52 333.5 32 302.5 32c-63.13 0-26.36 76.15-108.2 141.6l-16.3 13c-11.8 9.5-17.8 23.4-17.9 37.4c-.023.023 0 0 0 0l-.1 160c0 15.1 7.113 29.33 19.2 38.39l34.14 25.59C241 468.8 274.7 480 309.3 480H368c26.52 0 48-21.47 48-47.98c0-3.635-.48-7.143-1.246-10.55C434 415.2 448 397.4 448 376c0-9.148-2.697-17.61-7.139-24.88C463.1 347 480 327.5 480 304.1c0-12.5-4.893-23.78-12.72-32.32C492.2 270.1 512 249.5 512 224.1z"
      />
    </svg> {{ likes }} likes
    </span>
    <span v-else>
        <svg @click="deletedlike()" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                    <path
                      fill="currentColor"
                      d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1c0-16.8-14.3-32-32-32zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99a23.88 23.88 0 0 0 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59a23.934 23.934 0 0 0-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66.86-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51a23.851 23.851 0 0 0-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83a65.97 65.97 0 0 0-.64-9.122c17.84-12.15 29.28-32.58 29.28-55.28a66.33 66.33 0 0 0-1.876-15.64C499.9 270.1 512 250.2 512 227z"
                    />
                  </svg> {{ likes }} likes
    </span>
    </span>
    <span v-else>
      <svg  xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512">
                    <path
                      fill="currentColor"
                      d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1c0-16.8-14.3-32-32-32zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99a23.88 23.88 0 0 0 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59a23.934 23.934 0 0 0-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66.86-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51a23.851 23.851 0 0 0-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83a65.97 65.97 0 0 0-.64-9.122c17.84-12.15 29.28-32.58 29.28-55.28a66.33 66.33 0 0 0-1.876-15.64C499.9 270.1 512 250.2 512 227z"
                    />
                  </svg> {{ likes }} likes
    </span>
</template>

<script>
import {mapGetters,mapActions} from 'vuex'
import axios from 'axios'
export default {
  props: {
      replyid:{
      type: Number,
        },
        userprofile:{
        type: Number,
        },
        userentreprise:{
        type: Number,
        },
  },
  data() {
    return {
        reply:[],
        liked:false,
        changed:false,
        likes:0
    }
  },
  computed: {
    ...mapGetters({
      Votes: 'StateVotes',
      
    }),},
  methods:{
    ...mapActions(['GetVotes','CreateNotification','CreateVote']),
    likedreply(){
        this.liked=false
        axios.post('/reply/reply-update/'+this.replyid+'/',{nblikesR:this.likes-1})
        for (let v in this.Votes) {
        if (this.Votes[v].replyVo === this.replyid && (this.Votes[v].userprofileVo === this.userprofile ||this.Votes[v].userentrepriseVo === this.userentreprise)) {
          axios.delete('/vote/vote-delete/' + this.Votes[v].id + '/');
        }
      }
      this.likes-=1
    },
    deletedlike(){
        this.liked=true
        this.CreateVote({ replyVo: this.replyid, userprofileVo: this.userprofile, userentrepriseVo:this.userentreprise });
        axios.post('/reply/reply-update/' + this.replyid + '/', {nblikesR: this.likes+1});
        this.likes+=1
        /*if(this.CurrentUserProfile.id!=this.question.userprofileQ){
          this.CreateNotification({message:' liked your reply !',userprofileNo:this.userprofile,replyNo:this.replyid})
      }*/
         

        
    }
  },
  
  created(){
      this.GetVotes()
      axios.get('/reply/reply-detail/' + this.replyid + '/').then((response) => {
          this.reply = response.data;
          this.likes = this.reply.nblikesR
          for(let v in this.Votes){
            if(this.userprofile==this.Votes[v].userprofileVo && this.Votes[v].replyVo==this.reply.id){
               
                this.liked=true
            }else if (this.userentreprise==this.Votes[v].userentrepriseVo && this.Votes[v].replyVo==this.reply.id)
            {
              this.liked=true
            }
        }
        });
        
        
  }
};
</script>
