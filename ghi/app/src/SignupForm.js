import React, { useState } from 'react';

const SignupForm = () => {
  const [firstname, setFirstName] = useState('');
  const [lastname, setLastName] = useState('');
  const [birthday, setBirthday] = useState('');
  const [photo, setPhoto] = useState('');
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState('');
  const [join, setJoin] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = {}
    data.firstname = firstname
    data.lastname = lastname
    data.birthday = birthday
    data.photo = photo
    data.email = email
    data.status = status
    data.join = join

    const userUrl = 'http://localhost:8082/api/users'
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      },
    }
    const userResponse = await fetch(userUrl, fetchConfig)
    if (userResponse.ok) {
      setFirstName('')
      setLastName('')
      setBirthday('')
      setPhoto('')
      setEmail('')
      setStatus('')
      setJoin('')
    }
  }
  const handleFirstNameChange = (event) => {
    const value = event.target.value
    setFirstName(value)
  }

  const handleBirthdayChange = (event) => {
    const value = event.target.value
    setBirthday(value)
  }

  const handlePhotoChange = (event) => {
    const value = event.target.value
    setPhoto(value)
  }

  const handleEmailChange = (event) => {
    const value = event.target.value
    setEmail(value)
  }

  const handleStatusChange = (event) => {
    const value = event.target.value
    setStatus(value)
  }

  const handleJoinChange = (event) => {
    const value = event.target.value
    setJoin(value)
  }


  return (
<div class="modal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body"></div>






    <div>
      <div className="row">
        <div className="offset-3 col-6">
          <div className="shadow p-4 mt-4">
            <h1>Sign Up</h1>
            <form onSubmit={handleSubmit}></form>

            <div className="form-cloating mb-3">
              <input value={firstname} onChange={handleFirstNameChange} name="firstname" placeholder="First Name" id="name" required type="text" className="form-control" />
            </div>

            <div className="form-cloating mb-3">
              <input value={birthday} onChange={handleBirthdayChange} name="Birthday" placeholder="Birthday" id="birthday" required type="date" className="form-control" />
              <label>Date of Birth</label>
            </div>

          </div>
        </div>
      </div>




      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>




    </div>);// end of return
};//end of function

export default SignupForm;
