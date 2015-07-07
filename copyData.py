import os
import sys
import optparse

# Bristol SE: lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/user
# Imperial SE: gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms%s'
# CERN SE: eoscms.cern.ch//eos/cms

bristol = "soolin.phy.bris.ac.uk"
imperial = "ic.ac.uk"
cern = "cern.ch"

##__________________________________________________________
def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('-l','--ls',action='store_true',default=False, help="List samples in SE")
    parser.add_option("--dry-run", action = "store_true", default = False, help = "do not run any commands; only print them")
    (options,args) = parser.parse_args()
                
    return options

##__________________________________________________________
def _check_host(host, user):
    """
    List samples of SE of current HOST
    """
    
    if cern in host:
         SEdir = 'srm://srm-eoscms.cern.ch//eos/cms/store/data'
         _listSamples(host, user, SEdir)
    elif bristol in host:
        SEdir = 'gsiftp://lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/user/dosmith'
        _listSamples(host,user,SEdir)
    elif imperial in host:
        SEdir = 'srm://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/'
        _listSamples(host,user,SEdir)
    else:
        sys.exit("HOST not found")



##____________________________________________________________
def _listSamples(host, user, SEdir):

    options = parse_args()

    cmd = ['gfal-ls']
    cmd.append(SEdir)
    cmd = ' '.join(cmd)
    if options.dry_run:
        print cmd
    else:
        os.system(cmd)

    

##____________________________________________________________
def main():

    try:
        host = os.environ["HOSTNAME"]
        user = os.environ["USER"]
    except Exception, e:
        print >> sys.stderr, "HOST does not exist"
        print >> sys.stderr, "Exception: %s" % str(e)
        sys.exit(1)
        
    _check_host(host, user)



##____________________________________________________________
if __name__ == '__main__':
    """
    Define HOST names
    """

    """
    Run main()
    """
    main()
