DESTDIR:=""
PREFIX:=/usr
DATADIR:=${PREFIX}/share
GDESKLETSDIR:=${DATADIR}/gdesklets
NAME:=gdesklets-citation

install:
	mkdir -p ${DESTDIR}/${GDESKLETSDIR}/Displays/${NAME}/bg
	cp      -rp    bg               ${DESTDIR}/${GDESKLETSDIR}/Displays/${NAME}/
	install -m0644 citation.display ${DESTDIR}/${GDESKLETSDIR}/Displays/${NAME}/
	install -m0644 citation.py      ${DESTDIR}/${GDESKLETSDIR}/Displays/${NAME}/
	install -m0644 citation.png     ${DESTDIR}/${GDESKLETSDIR}/Displays/${NAME}/
	
