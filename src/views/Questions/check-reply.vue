<template>
    <span v-if="userprofile!=null">
    <span v-if="checked==true">
        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="3em" height="3em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="#62b47d" fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm8.854-9.646a.5.5 0 0 0-.708-.708L7.5 7.793L6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/></svg>
    </span>
    <span v-else-if="userprofile==currentuserprofile && checked==false">
        <svg  @click="checkreply()" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="3em" height="3em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><g fill="currentColor"><path fill-rule="evenodd" d="M10.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/></g></svg>
    </span>
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
        currentuserprofile:{
        type: Number,
        },
  },
  data() {
    return {
        reply:[],
        checked:false,
    }
  },
  computed: {
    ...mapGetters({
      Votes: 'StateVotes',
      
    }),},
  methods:{
    ...mapActions(['GetVotes','CreateVote']),
    checkreply(){
        axios.post('/reply/reply-update/'+this.replyid+'/',{checked:true})
        this.$router.go()
    },
  },
  
  created(){
      axios.get('/reply/reply-detail/' + this.replyid + '/').then((response) => {
          this.reply = response.data;
          this.checked = this.reply.checked
          
        });
        
        
  }
};
</script>
