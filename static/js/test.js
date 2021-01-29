    // the overlay 
    $(".pics .row div").mouseenter(function () {

        $(this).children(".overlay").addClass("active");
        $(this).children("img").css("boxShadow", "none");
    })
    $(".pics .row div").mouseleave(function () {
        $(".pics .row div .overlay").removeClass("active");
        $(this).children("img").css("boxShadow", "6px 7px #999")
    })
    $(".pics .row div").click(function () {
        $(".pics .row div .overlay").removeClass("active");
        $(this).children(".overlay").toggleClass("active");
    })
    // like button 
    $(".pics .row div i").click(function () {
        $(this).toggleClass("active");
    })