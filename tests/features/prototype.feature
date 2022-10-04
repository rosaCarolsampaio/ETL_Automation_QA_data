@regression 
Feature: verification of any null values in the tables per field
  As a data qualitu engineer,
  I want to find any null values in a table,
  So I can learn communicate and improve the data quality.

  Scenario: Basic validatioon of null values per fields
    Given I connect the database "db-dev"
    # When  check if have any null values in the "items"
    # Then the result is showin and should not have any null values
    # Examples:
    #     | database |
    #     |  db-dev |