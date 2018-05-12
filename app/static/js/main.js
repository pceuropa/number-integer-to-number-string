new Vue({
   delimiters: ['[[', ']]'],
   el: '#app',
   data: {
      number: '',
      number_in_string: '',
   },
   watch: {
      number: function(){
         this.sendNumber()
      }
   },
   methods: {
      sendNumber:_.debounce( function(){
          var app = this
          axios.get('?n=' + this.number)
            .then(function(response){
                app.number_in_string = response.data.number
          })
          .catch(function(error){
            console.log(error)
          })
      }, 500)
   }
})
