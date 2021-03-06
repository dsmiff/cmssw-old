#ifndef CommonTools_Utils_AndCombiner_h
#define CommonTools_Utils_AndCombiner_h
/* \class reco::parser::AndCombiner
 *
 * logical AND combiner
 *
 * \author original version: Chris Jones, Cornell, 
 *         adapted to Reflex by Luca Lista, INFN
 *
 * \version $Revision: 1.1 $
 *
 */
#include "CommonTools/Utils/src/SelectorBase.h"
#include "CommonTools/Utils/src/SelectorPtr.h"

namespace reco {
  namespace parser {    
     struct AndCombiner : public SelectorBase {
      AndCombiner(SelectorPtr lhs, SelectorPtr rhs) :
	lhs_(lhs), rhs_(rhs) { }
      virtual bool operator()(const Reflex::Object& o) const {
	return (*lhs_)(o) && (*rhs_)(o);
      }
    private:
      SelectorPtr lhs_, rhs_;
    };
  }
}

#endif
