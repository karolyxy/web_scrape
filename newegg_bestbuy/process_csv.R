# read all scraped csv, and transfrom them to dataframe
newegg_chromebook <- read.csv('./newegg_bestbuy/newegg_chromebook.csv', stringsAsFactors = FALSE)
# name all columnes
colnames(newegg_chromebook) <- c('title', 'model', 'price')
newegg_chromebook$model = gsub("Model #: ", '', newegg_chromebook$model)

newegg_gaminglaptop <- read.csv('./newegg_bestbuy/newegg_gamingLaptop.csv', stringsAsFactors = FALSE)
# name all columnes
colnames(newegg_gaminglaptop) <- c('title', 'model', 'price')
# clean unnecessary info
newegg_gaminglaptop$price <- gsub("\\(.*","", newegg_gaminglaptop$price) 
newegg_gaminglaptop$price <- gsub(" ", "", newegg_gaminglaptop$price)
newegg_gaminglaptop$model = gsub("Model #: ", '', newegg_gaminglaptop$model)

newegg_businesslaptop <- read.csv("./newegg_bestbuy/newegg_businessLaptop.csv", stringsAsFactors = FALSE)
# name all columnes
colnames(newegg_businesslaptop) <- c('title', 'model', 'price')
# clean unnecessary info
newegg_businesslaptop <- newegg_businesslaptop[rowSums(newegg_businesslaptop=="")!=ncol(newegg_businesslaptop), ]
newegg_businesslaptop$price <- gsub("\\ .*","", newegg_businesslaptop$price) 
newegg_businesslaptop$model = gsub("Model #: ", '', newegg_businesslaptop$model)

write.csv(newegg_chromebook, file = "./newegg_chromebook.csv")
write.csv(newegg_gaminglaptop, file = "./newegg_gamingLaptop.csv")
write.csv(newegg_businesslaptop, file = "./newegg_businessLaptop.csv")


### BestBuy Laptops
bestbuy_chromebook <- read.csv('./newegg_bestbuy/bestbuy_chromebook.csv', stringsAsFactors = FALSE)
bestbuy_chromebook <- bestbuy_chromebook[, c(3, 1, 2)]
bestbuy_chromebook$model <- gsub(",", "", bestbuy_chromebook$model)
write.csv(bestbuy_chromebook, file = "./bestbuy_chromebook.csv")

bestbuy_gaminglaptop <- read.csv('./newegg_bestbuy/bestbuy_gamingLaptop.csv', stringsAsFactors = FALSE)
bestbuy_gaminglaptop <- bestbuy_gaminglaptop[, c(3, 1, 2)]
bestbuy_gaminglaptop$model <- gsub(",", "", bestbuy_gaminglaptop$model)
write.csv(bestbuy_gaminglaptop, file = "./bestbuy_gaminglaptop.csv")

bestbuy_businesslaptop <- read.csv('./newegg_bestbuy/bestbuy_businessLaptop.csv', stringsAsFactors = FALSE)
bestbuy_businesslaptop <- bestbuy_businesslaptop[, c(3, 1, 2)]
bestbuy_businesslaptop$model <- gsub(",", "", bestbuy_businesslaptop$model)
write.csv(bestbuy_businesslaptop, file = "./bestbuy_busineslaptop.csv")


