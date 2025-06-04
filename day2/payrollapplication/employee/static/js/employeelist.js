$(document).ready(function() {
    // alert("Employee List Page Loaded");
    $.ajax({
        url: '/list/data',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            console.log(response.data);
            console.log(response.columns);
            $('#employeeTable').DataTable({
                data: response.data,   
                columns: response.columns, 
            })

        },
        error: function(xhr, status, error) {
            console.error('Error fetching employee data:', error);
        }
    });
})