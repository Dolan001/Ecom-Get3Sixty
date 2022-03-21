<template>
  <div class="page-sign-up">
      <div class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Sign up</h1>
              <form @submit.prevent="submitForm">

                  <div class="field">
                      <label>Username</label>
                      <div class="control">
                          <input type="text" class="input" v-model="username">
                      </div>
                  </div>

                  <div class="field">
                      <label>Password (Must be at least 8 charecters including letters and numbers)</label>
                      <div class="control">
                          <input type="password" class="input" v-model="password">
                      </div>
                  </div>

                  <div class="field">
                      <label>Repeat password</label>
                      <div class="control">
                          <input type="password" class="input" v-model="password2">
                      </div>
                  </div>

                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="error in errors" :key="error">{{error}}</p>
                  </div>

                  <div class="field">
                      <div class="control">
                          <button class="button is-dark">Sign up</button>
                        </div>                  
                  </div>

                  <hr>

                  Or <router-link to="/log-in">click here</router-link> to log in!

              </form>
          </div>
      </div>

  </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'SignUp',
    data(){
        return{
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        submitForm(){
            this.errors = []

            if (this.username === ''){
                this.errors.push('The username is missing')
            }
            if(this.password === ''){
                this.errors.push('The password field is empty')
            }
            if(this.password !== this.password2){
                this.errors.push('The password doesn\'t match')
            }

            if (!this.errors.length){
                const formData = {
                    username : this.username,
                    password : this.password
                }

                console.log(this.username, this.password)

                axios
                    .post('/api/v1/users/', formData)
                    .then(res => {
                        toast({
                            message: 'Account created, please log in',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'top-center'
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(err => {
                        if (err.res){
                            for(const property in err.res.data){
                                this.errors.push(`${property}: ${err.res.data[property]}`)
                            }
                            console.log(JSON.stringify(err.res.data))
                        } else if (err.message){
                            this.errors.push('Something went wrong, please try again')
                            console.log(JSON.stringify(err))

                        }
                    })
            }

        }
    },

}
</script>

<style>

</style>