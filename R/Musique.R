library(ggplot2)
library(reshape2)
library(dplyr)
library(RColorBrewer)


subscription <- data.frame(y=c("2014","2015","2016","2017"), p =c("10.8","22.7","35.3","7.7")) 

head(subscription)

p <- ggplot(data=subscription, aes(x=y, y=p)) +
  geom_bar(color = "blue", fill=rgb(0.1,0.5,0.8,0.7), stat="identity") +
  labs(x = "Années", y = "Millions") +
  ggtitle(label = "Augmentation du nombre de souscriptions à un abonnement premium sur 4 ans")

p + scale_y_discrete(labels=c("10.8" = "7.7", "22.7" = "10.8",
                              "35.3" = "22.7", "7.7" = "35.3"))

############################################################################################
  
vinyl <- data.frame(age = c("18-24", "25-34", "35-44", "45-54", "55-64"), perc = c("16","33", "22", "18", "11")) 
head (vinyl)

ggplot(data=vinyl, aes(x=age, y=perc)) +
  geom_bar(color = "red", fill=rgb(0.2,0.3,0.2,0.6), stat="identity") +
  labs(x = "Tranches d'âge", y = "Pourcentage") +
  ggtitle(label = "Quel âge ont les acheteurs de vinyl ?")



#############################################################################################


str <- data.frame(an = c("2011","2012","2013","2014","2015","2016"), per = c("15","21","27","34","51","9"))
head(str)

s <- ggplot(data=str, aes(x=an, y=per)) +
  geom_bar(color = "green", fill=rgb(0.7,0.3,0.9,0.6), stat="identity") +
  labs(x = "Années", y = "Pourcentage") +
  ggtitle(label = "Proportions des revenus générés par le streaming pour l'industrie musicale des USA")

s + scale_y_discrete(labels=c("15" = "9", "21" = "15",
                              "27" = "21", "34" = "27", "51"="34","9"="51"))


###############################################################################################

uni <- data.frame(ann = c("2007","2008","2009","2010","2011","2012","2013","2014","2015"), un=c("500.5","428.4","373.9","326.2","331","316","289.4","257","241.4"))
head(uni)

u <- ggplot(data=uni, aes(x=ann, y=un)) +
  geom_bar(color = "green", fill=rgb(0.9,0.8,0.7,0.6), stat="identity") +
  labs(x = "Années", y = "Millions") +
  ggtitle(label = "Ventes annuelles d'albums en format CD aux Etats-Unis")

u

###########################################################################"

cif <- data.frame(
  tot = rep(c("phys", "num"), each = 18),
  j = rep(c("1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"),2),
  len = c("23.8", "23.3", "23", "21.4", "19.8", "19.2", "17.9", "16.3", "14.1", "11.9", "10.4", "8.8", "8.2", "7.8", "6.8", "6.1", "5.8", "5.4",
          "0", "0", "0", "0", "0", "0.4", "1.1", "2.1","2.9", "3.7", "4.1", "4.3", "4.9", "5.4", "5.7", "6", "6.6", "7.6")
)

library(dplyr)
cif2 <- cif %>%
  group_by(j) %>%
  arrange(j, desc(tot)) %>%
  mutate(lab_ypos = len)
  
cif2





c <- ggplot(cif, aes(x=j, y = as.numeric(levels(cif$len))[cif$len])) + 
  geom_col(aes(fill = tot), width = 0.7) + 
  geom_text(size = 3, aes(label = len), position = position_stack(vjust = 0.5), color = "white") +
  scale_fill_discrete(labels = c("Numérique", "Physique"))+
  theme(legend.title = element_blank())+
  labs(x = "Années", y = "Total des revenus (Mds $USD)") +
  ggtitle(label = "Chiffre d'affaires mondial de la musique enregistrée 1999-2016")
  
c



###############################################
numerique <- data.frame(
  anne = c("2015", "2016", "2017", "2018", "2019", "2020"),
  taux = c("11.7", "13", "13.8", "14.5", "15", "15.7")
)

n <- ggplot(data=numerique, aes(x=anne, y=taux)) +
  geom_bar(color = "green", fill=rgb(0.7,0.9,0.2,0.6), stat="identity") +
  labs(x = "Années", y = "Milliards $USD") +
  ggtitle(label = "Taux des ventes numériques de musique")

n



###############################################################
rem <- data.frame(
  serv = c("Napster", "Tidal", "Apple Music", "Google Play Music", "Deezer", "Spotify", "Pandora Premium", "Youtube"),
  ec = c("0.016", "0.011", "0.0064", "0.0059", "0.0056", "0.0038", "0.0011", "0.0006")
)

r <- ggplot(data=rem, aes(x=serv, y=ec)) +
  geom_bar(color = "green", fill=rgb(0.6,0.7,0.8,0.9), stat="identity") +
  labs(x = "Service", y = "Rémunération par écoute ($USD)")

r

###############################################################
pirat <- data.frame(
  pir = c("Piratage de musique", "Stream Ripping", "Téléchargements illégaux", "Autres Pratiques"),
  pourc = c("35", "30", "20","15")
)

bp <- ggplot(pirat, aes(x="", y=pourc, fill=pir))+
  geom_bar(width = 1, stat = "identity")


p <- bp + coord_polar("y", start=0) + 
  scale_fill_brewer(palette = "BuPu") +
  ggtitle(label = "L'illégalité dans l'industrie de la musique") +
  theme(legend.title = element_blank(), axis.title.x = element_blank(), axis.title.y=element_blank(), axis.text = element_blank(), axis.ticks = element_blank(), panel.grid = element_blank())
p


#####################
turntable <- data.frame(
  people = c("N'ont pas de tourne-disque", "Ont un tourne-disque qu'ils utilisent", "Ont un tourne disque mais ne l'utilisent pas"),
  stat = c("7", "52", "41")
)

bt <- ggplot(turntable, aes(x="", y=stat, fill=people))+
  geom_bar(width = 1, stat = "identity")


t <- bt + coord_polar("y", start=0) + 
  scale_fill_brewer(palette = "Spectral") +
  ggtitle(label = "Les personnes achetant des vinyls...") +
  theme(legend.title = element_blank(), axis.title.x = element_blank(), axis.title.y=element_blank(), axis.text = element_blank(), axis.ticks = element_blank(), panel.grid = element_blank())
t









