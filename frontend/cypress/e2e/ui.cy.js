describe('GUI Tests', () => {
  // define variables that we need on multiple occasions
  let uid // user id
  let name // name of the user (firstName + ' ' + lastName)
  
  before(function () {
    // create a fabricated user from a fixture
    cy.fixture('user.json')
      .then((user) => {
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/users/create',
          form: true,
          body: user
        }).then((response) => {
          uid = response.body._id.$oid
          name = user.firstName + ' ' + user.lastName
        })
      })
  })

  beforeEach(function () {
    // enter the main main page
    cy.visit('http://localhost:3000')
  })

  it('starting out on the landing screen', () => {
    // make sure the landing page contains a header with "login"
    cy.get('h1')
      .should('contain.text', 'Login')
  })

  it('login to the system with an existing account', () => {
    // detect a div which contains "Email Address", find the input and type (in a declarative way)
    cy.contains('div', 'Email Address')
      .find('input[type=text]')
      .type('test.test@test.com')

    // submit the form on this page
    cy.get('form')
      .submit()

    // assert that the user is now logged in
    cy.get('h1')
      .should('contain.text', 'Your tasks, ' + name)
  })

  // R8UC1, create a new todo item with description
  it('Check if input field exists', () => {
    cy.get('.inline-form')
      .find('input[type=text]')
      .should('exist');
  })

  it('Description check if empty or not', () => {
    cy.get('.inline-form')
      .find('input[type=text]')
      .should('have.value', '');
  })

  it('Description empty and the add-button should be disabled', () => {
    cy.get('.inline-form')
      .find('input[type=submit]')
      .should('be.disabled');
  })

  it('description not empty and the add-button should be enabled and the new item description should be added to the bottom of the list', () => {
    cy.get('.inline-form')
      .find('input[type=text]')
      .type('todo item 1');

    cy.get('.inline-form')
      .find('input[type=submit]')
      .click();

    cy.get('li.todo-item').last().contains('todo item 1');
  })

  // R8UC2, click on icon

  it('todo item is struck through', () => {
    cy.get('li.todo-item')
      .find('span.checker')
      .first()
      .click();

    cy.get('li.todo-item')
      .should('have.class', 'checked');
  })

  it('todo item is not struck through', () => {
    cy.get('li.todo-item')
      .find('span.checker')
      .first()
      .click();

    cy.get('li.todo-item')
      .find('span.checker')
      .first()
      .click();

    cy.get('li.todo-item')
      .should('not.have.class', 'checked');
  })

  // R8UC3, click on the x symbol
  it('Todo element deleted', () => {
    cy.contains('.todo-item', 'Watch video')
      .find('.span.remover')
      .click()
    cy.contains('.todo-item', 'Watch video')
      .should('not.exist')
  })

  after(function () {
    // clean up by deleting the user from the database
    cy.request({
      method: 'DELETE',
      url: `http://localhost:5000/users/${uid}`
    }).then((response) => {
      cy.log(response.body)
    })
  })
})
