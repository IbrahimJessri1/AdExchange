adcontents = document.getElementsByTagName('adcontent')

function parser(obj){
    if(!obj.children || obj.children.length == 0){
        let value = obj.getAttribute('value')
        let type = obj.getAttribute('type')
        if(type == 'int')
            return parseInt(value)
        if(type == 'float')
            return parseFloat(value)
        if(type == 'list'){
            return value.split('|')
        }
        return value
    }
    let res = {}
    for(let i = 0 ; i < obj.children.length; i++){
        let child = obj.children[i]
        let tag_name = child.tagName.toLowerCase()
        res[tag_name] = parser(child)
    }
    return res
}


function validate_request(obj){
    if(obj['min_cpc'] == undefined)
        return 0
    if(obj['interactive'] == undefined)
        return 0
    if(!obj['type'] == undefined)
        return 0
    if(obj['payment_account'] == undefined)
        return 0
    if(obj['shape'] == undefined)
        return 0
    return 1
}

setInterval(function(){
    for(let i = 0 ; i < adcontents.length; i++){
        let ad_con = adcontents[i]
        let res = parser(ad_con)
        if(!validate_request(res))
            continue
        res['response_type'] = 'html'
        let req_url = "http://127.0.0.1:9999/ssp/request"
        if(res['interactive'] == 'true')
            req_url += "_interactive"
        delete res.interactive
        json_data = JSON.stringify(res);
        var t1 = new Date()
        $.ajax({
            url:req_url,
            type: "POST",
            contentType: "application/json",
            data: json_data,
            dataType: 'json',
            success: function (result){
                // ad_con.innerHTML = result
                // console.log(result)
                document.write(result)
                var t2 = new Date()
                console.log(t2 - t1)
            },
            error: function(error){
                console.log(error)
            }
                
        })
        
    
    }

}, 10);