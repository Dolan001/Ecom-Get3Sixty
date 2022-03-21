<template>
    <div class="page-category">
        <div class="column is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{category.name}}</h2>
            </div>

            <ProductBox v-for="product in category.products" :key="product.id" :product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
import ProductBox from '../components/ProductBox.vue'

export default {
    name: 'Category',
    data(){
        return{
            category: {
                products: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    components:{
        ProductBox
    },
    //if same routes click after another(summer=>winter=>rain)
    watch:{
        $route(to, from){
            if(to.name === 'Category'){
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory(){
            const categorySlug = this.$route.params.category_slug

            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/api/v1/products/${categorySlug}`)
                .then(res => {
                    this.category = res.data
                    document.title = this.category.name + ' | Djackets'
                })
                .catch(err => {
                    console.log(err)

                    toast({
                        message: 'Something went wrong, try again',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'top-center'
                    })
                })

            this.$store.commit('setIsLoading', false)
        }
    },
}
</script>

<style>

</style>