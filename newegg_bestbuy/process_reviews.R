#bestbuy chromebook review
chromebook_review <- read.csv('./newegg_bestbuy/bestbuy_chromebookReview.csv', stringsAsFactors = FALSE)
chromebook_review <- chromebook_review[, c(2, 3, 4, 6, 7, 1, 5)]
write.csv(chromebook_review, file = "./chromebook_reviews.csv")

#bestbuy business laptop review
businesslaptop_review <- read.csv('./newegg_bestbuy/bestbuy_businessLaptopReview.csv', stringsAsFactors = FALSE)
businesslaptop_review <- businesslaptop_review[, c(5, 1, 7, 2, 4, 3, 6)]
write.csv(businesslaptop_review, file = "./businessLaptop_reviews.csv")

#bestbuy gaming laptop review
gaminglaptop_review <- read.csv('./newegg_bestbuy/bestbuy_gamingLaptopReview.csv', stringsAsFactors = FALSE)
gaminglaptop_review <- gaminglaptop_review[, c(6, 3, 2, 7, 1, 4, 5)]
write.csv(gaminglaptop_review, file = './gamingLaptop_reviews.csv')

### 込込込込込込