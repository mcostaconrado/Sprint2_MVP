/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  /*
  let url = 'http://127.0.0.1:5000/pacientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => insertList(item.name, 
                                                item.preg, 
                                                item.plas,
                                                item.pres,
                                                item.skin,
                                                item.test,
                                                item.mass,
                                                item.pedi,
                                                item.age,
                                                item.outcome
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
    */
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()




/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputAdults, inputChildren, inputWeekendNights, inputWeekNights, inputCar, inputLeadTime, inputMonth, inputDay, inputRepGuest,
  inputPrevCanc, inputPrevNotCanc, inputPrice, inputRequests) => {
    
  const formData = new FormData();
  formData.append('no_of_adults', inputAdults);
  formData.append('no_of_children', inputChildren);
  formData.append('no_of_weekend_nights', inputWeekendNights);
  formData.append('no_of_week_nights', inputWeekNights);
  formData.append('required_car_parking_space', inputCar);
  formData.append('lead_time', inputLeadTime);
  formData.append('arrival_month', inputMonth);
  formData.append('arrival_date', inputDay);
  formData.append('repeated_guest', inputRepGuest);
  formData.append('no_of_previous_cancellations', inputPrevCanc);
  formData.append('no_of_previous_bookings_Not_Cancelled', inputPrevNotCanc);
  formData.append('avg_price_per_room', inputPrice);
  formData.append('no_of_special_requests', inputRequests);



  let url = 'http://127.0.0.1:5000/reserva';
  
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then((data) => {
      let message = "";
      if (data.outcome)
        message = "Guest will not cancel";
      else
        message = "Gest will cancel";

      alert("Prediction: " + message)
    })
    .catch((error) => { 
      console.error('Error:', error);
    });

}

const newItem = async () => {
  let inputAdults = document.getElementById("new_no_of_adults").value;
  let inputChildren = document.getElementById("new_no_of_children").value;
  let inputWeekendNights = document.getElementById("new_no_of_weekend_nights").value;
  let inputWeekNights = document.getElementById("new_no_of_week_nights").value;
  let inputCar = document.getElementById("new_required_car_parking_space").value;
  let inputLeadTime = document.getElementById("new_lead_time").value;
  let inputMonth = document.getElementById("new_arrival_month").value;
  let inputDay = document.getElementById("new_arrival_date").value;
  let inputRepGuest = document.getElementById("new_repeated_guest").value;
  let inputPrevCanc = document.getElementById("new_no_of_previous_cancellations").value;
  let inputPrevNotCanc = document.getElementById("new_no_of_previous_bookings_Not_Cancelled").value;
  let inputPrice = document.getElementById("new_avg_price_per_room").value;
  let inputRequests = document.getElementById("new_no_of_requests").value;

  postItem(inputAdults, inputChildren, inputWeekendNights, inputWeekNights, inputCar, inputLeadTime, inputMonth, inputDay, inputRepGuest,
    inputPrevCanc, inputPrevNotCanc, inputPrice, inputRequests);

  } 