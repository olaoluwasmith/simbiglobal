$(function () {
    $(document).on('change', 'select#id_category', function () {
        $.getJSON('/getSubcategory_agric/', { id: $(this).val() }, function (j) {
            var options = "<option value=''>----------</option>";
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].id + '">' + j[i].name + "</option>";
            }

            $('select#id_subcategory').html(options);
        });
    });

    
});

$(function () {
    $(document).on('change', 'select#id_category_log', function () {
        $.getJSON('/getSubcategory_log/', { id: $(this).val() }, function (j) {
            var options = "<option value=''>----------</option>";
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].id + '">' + j[i].name + "</option>";
            }

            $('select#id_subcategory_log').html(options);
        });
    });
});

$(function () {
    $(document).on('change', 'select#id_category_mer', function () {
        $.getJSON('/getSubcategory_mer/', { id: $(this).val() }, function (j) {
            var options = "<option value=''>----------</option>";
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].id + '">' + j[i].name + "</option>";
            }

            $('select#id_subcategory_mer').html(options);
        });
    });
});