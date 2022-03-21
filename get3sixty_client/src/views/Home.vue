<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Get3sixty
        </p>
        <p class="subtitle">
          The best online store for dress
        </p>
      </div>
    </section>
    <div class="columns is-multiline">

      <div class="column is-12">
        <h2 class="is-size-3 has-text-centered">Latest product</h2>
      </div>

      <ProductBox v-for="product in latestProducts" :key="product.id" :product="product" />

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'

export default {
  name: 'Home',
  data(){
    return{
      latestProducts:[]
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getlatestProducts()
    document.title = 'Home ' + '| Djackets'
  },
  methods: {
    async getlatestProducts(){
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/latest-products/')
        .then(res =>{
          this.latestProducts = res.data
        })
        .catch(err => {
          console.log(err)
        })
      this.$store.commit('setIsLoading', false)  
    }
  },
}
</script>

<style>

</style>
