# User Stories

## User Registration and Authentication

### User Story: User Registration
As a new user, I want to be able to create an account on the travel booking platform so that I can access the platform's features and make bookings.

#### Acceptance Criteria:
```gherkin
Given I am on the registration page
When I provide a valid email address, username, and password
And I click on the "Register" button
Then my account should be created
And I should be redirected to the login page
```


```gherkin
Given I am on the login page
When I provide my registered email address and password
And I click on the "Login" button
Then I should be logged in to my account
And I should be redirected to the user dashboard
```

```gherkin
Given I am on the flight search page
When I enter a valid origin, destination, and travel dates
And I click on the "Search" button
Then I should see a list of available flights matching my search criteria
And the search results should include flight details such as airline, flight number, departure time, arrival time, and price
```


```gherkin
Given I am on the flight search results page
When I select a desired flight
And I click on the "Book" button
Then I should be redirected to the booking confirmation page
And the booking confirmation page should display the flight details and total price
When I confirm the booking
Then I should receive a booking confirmation with a unique booking reference number
```


```gherkin
Given I am on the hotel search page
When I enter a valid location, check-in date, and check-out date
And I click on the "Search" button
Then I should see a list of available hotels matching my search criteria
And the search results should include hotel details such as name, address, room types, amenities, and price per night
```

```gherkin
Given I am on the hotel search results page
When I select a desired hotel and room type
And I click on the "Book" button
Then I should be redirected to the booking confirmation page
And the booking confirmation page should display the hotel and room details, check-in and check-out dates, and total price
When I confirm the booking
Then I should receive a booking confirmation with a unique booking reference number
```

```gherkin
Given I am on the rental car search page
When I enter a valid location and rental dates
And I click on the "Search" button
Then I should see a list of available rental cars matching my search criteria
And the search results should include car details such as car type, make, model, year, and price per day
```

```gherkin
Given I am on the rental car search results page
When I select a desired rental car
And I click on the "Book" button
Then I should be redirected to the booking confirmation page
And the booking confirmation page should display the car details,
    rental dates, and total price
When I confirm the booking
Then I should receive a booking confirmation
    with a unique booking reference number
```

```gherkin
Given I am logged in to my account
When I navigate to the "My Bookings" page
Then I should see a list of all my bookings
And each booking should display relevant details such as booking reference number, travel dates, and status
```

```gherkin
Given I am on the "My Bookings" page
When I select a booking that I want to cancel
And I click on the "Cancel Booking" button
Then I should see a confirmation message asking me to confirm the cancellation
When I confirm the cancellation
Then the booking should be marked as canceled
And I should receive a cancellation confirmation message
```

```gherkin
Given I have completed a booking
When I navigate to the "My Bookings" page
And I select the completed booking
Then I should see an option to submit a review and rating
When I click on the "Submit Review" button
Then I should be redirected to the review submission form
And the form should allow me to enter a rating and a comment
When I submit the review
Then the review should be associated with the booking
And I should see a confirmation message indicating that the review has been submitted successfully
```

```gherkin
Given I am on the search results page for flights, hotels, or rental cars
When I select a specific flight, hotel, or rental car
Then I should see a section displaying the reviews and ratings for that item
And the reviews should include the user's rating, comment, and submission date
```

## ERD

https://dbdiagram.io/d/Wanderella-666ca865a179551be6ee15fe