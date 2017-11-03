/**
 * Created by Aiden on 5/12/16.
 */
$(document).ready(function() {

	renew_data();

    $('#pro_num').on('input', function(e) {
    	renew_data();
    });

    $(".shiptype").bind('change click', function() {
        var shipfee = parseInt($(this).val());
        var product_total_price = parseInt($("#product_total_price").text());

        update_price_direct(shipfee, "estimated_price");
        update_price_direct(shipfee + product_total_price, "total_price");
    });
    
    $('#checkoutForm').submit(function(){
        $('#total_price2').val($('#total_price').html());
    });
});
function setShipType(id){
    $('#shiptype2').val(id);
}


function renew_data() {

    uprice = parseInt($('#unit_price').text());
    num = parseInt($('#pro_num').val());

    if (isNaN(num)) {
        num = 1;
    }
    update_price_direct(uprice * num, "sub_total_price", "product_total_price", "total_price");

    if ($('input[class=shiptype]:checked').length > 0) {
    	$('input[class=shiptype]:checked').trigger('click');
    }
}

function update_price_direct(value, ...input) {
    for (var i of input) {
        $("#" + i).text(value);
    }
}

//可在Javascript中使用如同C#中的string.format
//使用方式 : var fullName = String.format('Hello. My name is {0} {1}.', 'FirstName', 'LastName');
String.format = function ()
{
    var s = arguments[0];
    if (s == null) return "";
    for (var i = 0; i < arguments.length - 1; i++)
    {
        var reg = getStringFormatPlaceHolderRegEx(i);
        s = s.replace(reg, (arguments[i + 1] == null ? "" : arguments[i + 1]));
    }
    return cleanStringFormatResult(s);
}
//可在Javascript中使用如同C#中的string.format (對jQuery String的擴充方法)
//使用方式 : var fullName = 'Hello. My name is {0} {1}.'.format('FirstName', 'LastName');
String.prototype.format = function ()
{
    var txt = this.toString();
    for (var i = 0; i < arguments.length; i++)
    {
        var exp = getStringFormatPlaceHolderRegEx(i);
        txt = txt.replace(exp, (arguments[i] == null ? "" : arguments[i]));
    }
    return cleanStringFormatResult(txt);
}
//讓輸入的字串可以包含{}
function getStringFormatPlaceHolderRegEx(placeHolderIndex)
{
    return new RegExp('({)?\\{' + placeHolderIndex + '\\}(?!})', 'gm')
}
//當format格式有多餘的position時，就不會將多餘的position輸出
//ex:
// var fullName = 'Hello. My name is {0} {1} {2}.'.format('firstName', 'lastName');
// 輸出的 fullName 為 'firstName lastName', 而不會是 'firstName lastName {2}'
function cleanStringFormatResult(txt)
{
    if (txt == null) return "";
    return txt.replace(getStringFormatPlaceHolderRegEx("\\d+"), "");
}