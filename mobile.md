    <div class="app" style="background:none;top:8%;">
         <form id="form" role="form" action="/demo-upload" enctype="multipart/form-data" method="post">
            {% raw xsrf_form_html() %}
        
            <input type="file" id="InputFile" name="mypicture">
                
                <p style="font-size:14px;text-transform:none;text-align:left;">
                     1. Please choose the image to be updated and recognized.<br>
                     2. You must enter the right address of your email, because all the results will be sent to your email in one minute.<br>
                     3. If you are a new user and you need to know how to use this app, you can see the <a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/user-tutorial.md">tutorials and examples.</a>
                </p>
                
            <label><b>Email:</b></label>
            <input id="email" name="email" type="email">
            <input id="DemoKind" name="demokind" value="mobile" style="display:none">
            <button type="button" class="btn btn-default" id="submit_img">Submit</button>
        </form>
        <hr>
        
        <label><b>Power by ArchiCV</b></label><br>
        
        <p><a href="https://github.com/zhangxiansheng/-archi/blob/master/README.md">archiCV-tutorials</a> <br><a href="https://github.com/zhangxiansheng/-archi/blob/based-for-website-tmp/README.md">archicv-references</a></p>
        
    </div>
    
    
    
<script>
    $(document).ready(function(){
    if (localStorage.email)
    {
        $("#email").attr( "value", localStorage.email );
    }else{
    $("#email").attr( "value", "Enter your email here." );
    }
    });
    
    function getCookie(name) {
        var c = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return c ? c[1] : undefined;
    }

    $("#submit_img").click(function(){
                       $("#submit_img").attr("disabled","disabled");
                       $("#submit_img").html("Wait ...");
                       var fd = new FormData(document.getElementById("form"));
                       fd.append("_xsrf", getCookie("_xsrf"));
                       htmlobj = $.ajax({
                                        url: "/demo-upload",
                                        type: "POST",
                                        data: fd,
                                        processData: false,  // tell jQuery not to process the data
                                        contentType: false,   // tell jQuery not to set contentType
                                        success: function (){
                                        $("#submit_img").removeAttr("disabled");
                                        $("#submit_img").html("Submit");
                                        localStorage.email = $("#email").val();
                                            } //success
                                        });
                       });
</script>
