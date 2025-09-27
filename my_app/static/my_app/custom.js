$(document).ready(function(){
//     fill the bookmark sign
    $(document).on('click','save_fact',function(){
        let _vm=$(this);
        _vm.addClass('bi-bookmark-fill').removeClass('bi-bookmark')
    });
});