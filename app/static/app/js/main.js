// get product_name by category name 
$(function() {
    $("#category_id").on("change", function() {
        category_id = $(this).val();
        $.get(
            "/previsions/getProducts", {
                category_id: category_id
            },
            function(data) {
                $("id_product").html(data)
            }
        );
    });

});
// calculate total price of a product
$('#id_unit_price').on('keyup', function() {
    var unit_price = $(this).val();
    var id_quantite = $('#id_quantite').val();
    var total = id_quantite * unit_price;
    $('#id_total_price').val(total);
});
p