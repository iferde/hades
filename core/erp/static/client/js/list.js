var tbClient;

function getData() {
    tbClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "surnames"},
            {"data": "dni"},
            {"data": "date_birthday"},
            {"data": "gender"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}
$(function () {
    getData();

    $(".btnAdd").on('click', function() {
        $('input[name="action"]').val('add');
        //$('form')[0].reset(); // Limpiar el formulario
        $('#myModalClient').modal('show');
    })
    
    $("#myModalClient").on('show.bs.modal', function() {
        $('form')[0].reset(); // Limpiar el formulario
    })  

    $("form").on("submit", function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
    
        submit_with_ajax(
          window.location.pathname,
          "Notificación",
          "¿Estas seguro de realizar la siguiente acción?",
          parameters,
          function () {
            $('#myModalClient').modal('hide');
            tbClient.ajax.reload();
          }
        );
    });
});