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
    menuItem('Intro', tabName = 'intro', icon = icon('info'))
    ),
    dashboardBody()
  )

)