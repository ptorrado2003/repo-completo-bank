## Introduction

The IE Bank account management system is web designed to manage bank accounts. The objective of this document is to describe the requirements and design of the system, as well as its testing plan and release strategy. The system will be built using Vue.js as the front-end framework, Flask as the back-end framework, SQLAlchemy as the database ORM, and Azure Functions as the serverless computing platform.

## General System Description

The IE Bank Corp account management system is a web-based system that allows users to create, read, update, and delete bank accounts. The system also allows users to add a new field for the country of origin of each account. The system will be built using a microservices architecture, with separate services for authentication, authorization, and data storage. The front-end will be built using Vue.js, with a responsive design that adapts to different screen sizes and devices.

## System Context

The system will be used in a production environment and will be accessed through the web. The users will be employees of IE Bank Corp and customers of the company. The system will be deployed on Azure, using Azure Functions as the serverless computing platform.

## Assumptions

It is assumed that the users have basic knowledge of web navigation and have access to a stable internet connection. It is also assumed that the users have a valid account with IE Bank Corp.

## Constraints

The system must comply with the security and privacy standards of IE Bank Corp. The system must also be compatible with different web browsers and mobile devices. The system must be built using secure coding practices and must follow the principles of least privilege.

## Software Requirements

## Functional Requirements

The system must allow users to create, read, update, and delete bank accounts.
The system must allow users to add a new field for the country of origin of each account.
The system must validate the information entered by the user.
The system must use authentication and authorization to protect the information of the customers.
The system must use encryption to protect sensitive information.
Non-Functional Requirements

- Must be secure and protect the information of the customers.
- Must be scalable and able to handle a large volume of users.
- Must be compatible with different web browsers and mobile devices.
- Must be built using Vue.js, Flask, SQLAlchemy, and Azure Functions.

## Security

- Use authentication and authorization to protect the information of the customers.
- Use encryption to protect sensitive information.
- The system must be built using secure coding practices and must follow the principles of least privilege.
## Availability and Reliability

- Available 24 hours a day, 7 days a week.
- Must be reliable and not experience frequent interruptions.
- The system must be built using Azure Functions, which provides a highly available and scalable platform.
## Recoverability

- Have a disaster recovery plan.
- Have regular backups.
- The web must be built using Azure Functions, which - Provides a highly available and scalable platform.
Business Continuity

The system must have a business continuity plan in case of interruptions.
The system must be built using Azure Functions, which provides a highly available and scalable platform.
# Cost Management

- The backend must be built using Azure Functions, which provides a cost-effective platform.
- The frontend must be deployed on Netlify (Initial free)
- The system must be built using Vue.js, which provides a robust framework for building user interfaces.

# System Maintenance and Support

- Which provides a highly available and scalable platform.
# Software Modeling

Use Case and Sequential Model

The system must have a use case model that describes the interactions between the users and the system.
The system must have a sequential model that describes the sequence of events in the system.
The system must be built using Vue.js, which provides a robust framework for building user interfaces.
# Entity Relationship Diagram

The system must have an entity relationship diagram that describes the entities and relationships in the system.
The system must be built using SQLAlchemy, which provides a powerful ORM for working with databases.
# Data Flow Diagram

The system must have a data flow diagram that describes the flow of data in the system.
The system must be built using Azure Functions, which provides a highly available and scalable platform.
Design

# Infrastructure Architecture Design

The system must have an infrastructure architecture design that describes the infrastructure necessary for its launch.
The system must be built using Azure Functions, which provides a highly available and scalable platform.
# GUI Mockups

![App Screenshot](https://github.com/ptorrado2003/repo-completo-bank/blob/main/IE%20Bank/IE%20Bank/Screen%20Shot%202024-10-18%20at%2012.08.12%20PM.png)

![App Screenshot](https://github.com/ptorrado2003/repo-completo-bank/blob/main/IE%20Bank/IE%20Bank/Screen%20Shot%202024-10-18%20at%2012.31.55%20PM.png)

![App Screenshot](https://github.com/ptorrado2003/repo-completo-bank/blob/main/IE%20Bank/IE%20Bank/Screen%20Shot%202024-10-18%20at%2012.32.11%20PM.png)

# Environments Design

- Must have an environments design that describes the development, testing, and production environments.

- Database URL to locale deploy
# Release Strategy

The system must have a release strategy that describes the plan for its launch and promotion.
The system must be built using Azure Functions, which provides a highly available and scalable platform.
Software Quality Assurance (SQA)

# Test Plan

The system must have a test plan that describes the tests necessary to ensure the quality of the system.
The system must be built using Vue.js, Flask, SQLAlchemy, and Azure Functions.
The system must be tested using a combination of unit tests, integration tests, and end-to-end tests.
