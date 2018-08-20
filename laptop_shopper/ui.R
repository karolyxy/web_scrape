#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinydashboard)
library(data.table)
library(dplyr)
library(ggplot2)
library(tidyr)
library(DT)



shinyUI(
  dashboardPage(
    dashboardHeader(title = "Laptop Shopper"),
    dashboardSidebar(
      sidebarMenu(
        menuItem('Intro', tabName = 'intro', icon = icon('info')),
        menuItem('Price', tabName = 'price', icon = icon('balance-scale'),
                menuItem('Categroy', tabName = 'category', icon = icon('shopping-cart')),
                menuItem('Brand', tabName = 'brand', icon = icon('globe')),
                menuItem('Detail', tabName = 'detail', icon = icon('list'))),
        menuItem('About Customers', tabName = 'customer', icon = icon('user')),
        menuItem('Conclusion', tabName = 'conclusion', icon = icon('tasks'))
        )
      ),
    dashboardBody(
      
      #introduction tab
      tabItem(tabName = 'intro',
        fluidRow(
          
        )
      )
      
    )
  )
  
)
