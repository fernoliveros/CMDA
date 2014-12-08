cfb <- read.csv("data/cfb2013stats.csv")

library(ggplot2)

### Scatter Plot

cfb$PassRatio <- cfb$PassCompOff / cfb$PassAttOff
cfb$PassRatioCat <- cut(cfb$PassRatio,
                        breaks=c(0, 0.48, 0.72, 1),
                        labels=c('below', 'average', 'above'))


png('scatter.png')
ggplot(cfb, aes(x=cfb$PassAttOff,
                y=cfb$PassCompOff,
                color=cfb$PassRatioCat)) +
geom_point() +
scale_color_brewer(type='div', palette=4) +
xlab("Pass Attempts") +
ylab("Pass Completions") +
ggtitle("Passing Accuracy") +
scale_fill_discrete(name = "New Legend Title") +
theme(legend.title=element_blank())
dev.off()

### Histogram
cfb$ScoreDiff <- cfb$ScoreOff - cfb$ScoreDef

cfb$WL <- (ifelse(cfb$ScoreDiff > 0, "Win", "Loss"))

subH <- subset(cfb, cfb$Site == "H")
subH2 <- subset(subH, subH$Line != "NA")
subH2$LineDiff <- subH2$Line - subH2$ScoreDiff

png('hist.png')
h<-hist(subH2$LineDiff,
        col = "lightblue",
        nclass = 18,
        xlab = "Line and Score Difference",
        main = "Betting Line Predictions")

xfit<-seq(min(subH2$LineDiff),max(subH2$LineDiff),length=40) 
yfit<-dnorm(xfit,mean=mean(subH2$LineDiff),sd=sd(subH2$LineDiff)) 
yfit <- yfit*diff(h$mids[1:2])*length(subH2$LineDiff) 
lines(xfit, yfit, col="blue", lwd=2)
dev.off()

### Bar Plot
counts <- table(cfb$WL, cfb$Site)

png('bar.png')
barplot(counts,
        main="Home Field Advantage",
        xlab="Home Neutral Visitor",
        ylab="Frequency",
        col=c("lightblue","orange"),
        legend = rownames(counts),
        beside = TRUE)
dev.off()

### UVA vs. VT graph
# VT <- subset(cfb, cfb$TeamName == "Virginia Tech")
# UVA <- subset(cfb, cfb$TeamName == "Virginia")
# 
# xPassVT <- VT$PassAttOff
# yPassVT <- VT$PassYdsOff
# xRushVT <- VT$RushAttOff
# yRushVT <- VT$RushYdsOff
# 
# xPassUVA <- UVA$PassAttOff
# yPassUVA <- UVA$PassYdsOff
# xRushUVA <- UVA$RushAttOff
# yRushUVA <- UVA$RushYdsOff
# 
# xrange = c(25,63)
# yrange <- c(48, 391)
# yrange
# plot(xrange, yrange, type="n", xlab="Pass/Rush Attempts", ylab="Pass/Rush Yards")




